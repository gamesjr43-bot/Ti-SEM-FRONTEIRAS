# -*- coding: utf-8 -*-
"""
Camada de acesso a dados do TI Sem Fronteiras.

Tenta ler do Firestore (Firebase). Se não houver credencial configurada
(ainda não conectou o Firebase, ou está rodando localmente sem o arquivo
de chave), cai automaticamente para os dados mockados de data.py — assim
o app NUNCA quebra, mesmo antes da configuração do Firebase estar pronta.

Ordem de busca da credencial:
  1. st.secrets["firebase"]   -> usado no Streamlit Community Cloud (deploy online)
  2. ./serviceAccountKey.json -> usado no seu computador (teste local)
  3. Nenhuma encontrada       -> usa data.py (modo demonstração offline)
"""

import json
import os

import streamlit as st

import data  # fallback local

_db = None
_modo_atual = None  # "firestore" ou "local" — usado para mostrar na sidebar


def _tentar_conectar():
    """Inicializa o Firebase Admin SDK uma única vez. Retorna o client ou None."""
    global _db, _modo_atual

    if _db is not None:
        return _db
    if _modo_atual == "local":
        return None

    try:
        import firebase_admin
        from firebase_admin import credentials, firestore
    except ImportError:
        _modo_atual = "local"
        return None

    try:
        if not firebase_admin._apps:
            cred = None

            # 1) Credencial via secrets (deploy no Streamlit Community Cloud)
            if "firebase" in st.secrets:
                cred_info = dict(st.secrets["firebase"])
                cred = credentials.Certificate(cred_info)

            # 2) Credencial via arquivo local (teste na sua máquina)
            elif os.path.exists("serviceAccountKey.json"):
                cred = credentials.Certificate("serviceAccountKey.json")

            if cred is None:
                _modo_atual = "local"
                return None

            firebase_admin.initialize_app(cred)

        _db = firestore.client()
        _modo_atual = "firestore"
        return _db

    except Exception as e:
        st.sidebar.warning(f"Não foi possível conectar ao Firebase: {e}")
        _modo_atual = "local"
        return None


def modo_dados() -> str:
    """Retorna 'firestore' ou 'local', para exibir na interface."""
    _tentar_conectar()
    return _modo_atual or "local"


def _carregar_colecao(nome_colecao: str, fallback: list) -> list:
    db = _tentar_conectar()
    if db is None:
        return fallback
    try:
        docs = db.collection(nome_colecao).stream()
        registros = [doc.to_dict() for doc in docs]
        return registros if registros else fallback
    except Exception as e:
        st.sidebar.warning(f"Erro ao ler '{nome_colecao}' do Firestore: {e}")
        return fallback


def carregar_paises() -> list:
    return _carregar_colecao("paises", data.PAISES)


def carregar_vagas() -> list:
    return _carregar_colecao("vagas", data.VAGAS)


def carregar_radar_tecnologias() -> list:
    return _carregar_colecao("radar_tecnologias", data.RADAR_TECNOLOGIAS)


def carregar_trilhas_qualificacao() -> list:
    return _carregar_colecao("trilhas_qualificacao", data.TRILHAS_QUALIFICACAO)
