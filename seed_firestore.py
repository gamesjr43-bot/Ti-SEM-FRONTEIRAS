# -*- coding: utf-8 -*-
"""
Popula o Firestore com os dados de demonstração do TI Sem Fronteiras.

Coloque o arquivo serviceAccountKey.json na mesma pasta e rode:

    python3 seed_firestore.py             # envia/atualiza os dados
    python3 seed_firestore.py --limpar    # apaga as coleções antes de enviar (recomeça do zero)
    python3 seed_firestore.py --dry-run   # só mostra o que seria enviado, sem conectar

É seguro rodar várias vezes: cada documento tem um ID estável (ex.: "portugal"),
então rodar de novo ATUALIZA em vez de duplicar.

Coleções criadas: paises, vagas, radar_tecnologias, trilhas_qualificacao.
"""

import argparse
import os
import re
import sys
import unicodedata

import data

CHAVE = "serviceAccountKey.json"

# nome da coleção -> (função que gera o ID do documento, registros)
COLECOES = {
    "paises": (lambda r: r["pais"], data.PAISES),
    "vagas": (lambda r: f"{r['pais']} {r['empresa']} {r['titulo']}", data.VAGAS),
    "radar_tecnologias": (lambda r: r["tecnologia"], data.RADAR_TECNOLOGIAS),
    "trilhas_qualificacao": (lambda r: r["area"], data.TRILHAS_QUALIFICACAO),
}


def slug(texto: str) -> str:
    """'Docker / Kubernetes' -> 'docker_kubernetes'. Sem acentos, sem '/', seguro p/ ID do Firestore."""
    sem_acento = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", sem_acento.lower()).strip("_")


def validar():
    """Confere consistência dos dados antes de enviar. Retorna lista de erros."""
    erros = []
    paises = {p["pais"] for p in data.PAISES}
    for v in data.VAGAS:
        if v["pais"] not in paises:
            erros.append(f"Vaga '{v['titulo']}' aponta para país inexistente: {v['pais']}")
    for nome, (fid, registros) in COLECOES.items():
        ids = [slug(fid(r)) for r in registros]
        duplicados = {i for i in ids if ids.count(i) > 1}
        if duplicados:
            erros.append(f"IDs duplicados em '{nome}': {sorted(duplicados)}")
    return erros


def limpar_colecao(db, nome, tamanho_lote=400):
    docs = list(db.collection(nome).stream())
    for i in range(0, len(docs), tamanho_lote):
        lote = db.batch()
        for d in docs[i:i + tamanho_lote]:
            lote.delete(d.reference)
        lote.commit()
    return len(docs)


def enviar_colecao(db, nome, fid, registros):
    lote = db.batch()  # 1 escrita em lote por coleção (bem abaixo do limite de 500)
    for r in registros:
        lote.set(db.collection(nome).document(slug(fid(r))), r)
    lote.commit()


def main():
    ap = argparse.ArgumentParser(description="Popula o Firestore com dados de demonstração.")
    ap.add_argument("--limpar", action="store_true", help="apaga as coleções antes de enviar")
    ap.add_argument("--dry-run", action="store_true", help="não conecta; apenas lista o que enviaria")
    args = ap.parse_args()

    erros = validar()
    if erros:
        print("❌ Problemas nos dados de demonstração:")
        for e in erros:
            print("   -", e)
        sys.exit(1)

    if args.dry_run:
        for nome, (fid, registros) in COLECOES.items():
            print(f"📄 {nome}: {len(registros)} documento(s)")
            for r in registros:
                print(f"     {slug(fid(r))}")
        print("\n(dry-run: nada foi enviado)")
        return

    if not os.path.exists(CHAVE):
        print(f"❌ Não encontrei '{CHAVE}' nesta pasta.")
        print("   Baixe em: Firebase Console > Configurações do projeto")
        print("   > Contas de serviço > Gerar nova chave privada.")
        sys.exit(1)

    import firebase_admin
    from firebase_admin import credentials, firestore

    firebase_admin.initialize_app(credentials.Certificate(CHAVE))
    db = firestore.client()

    for nome, (fid, registros) in COLECOES.items():
        if args.limpar:
            print(f"🧹 '{nome}': {limpar_colecao(db, nome)} documento(s) removido(s).")
        enviar_colecao(db, nome, fid, registros)
        print(f"✅ '{nome}': {len(registros)} documento(s) enviado(s).")

    print("\n🎉 Firestore populado! Agora rode: streamlit run app.py")


if __name__ == "__main__":
    main()
