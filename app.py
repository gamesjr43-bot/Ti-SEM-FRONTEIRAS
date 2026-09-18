# -*- coding: utf-8 -*-
"""
TI Sem Fronteiras - Protótipo (SIRITEC / IFS Campus Socorro)

Ecossistema modular para internacionalização de carreiras em TI:
  - Módulo I  -> MundoDev      (Inteligência Geográfica)
  - Módulo II -> GlobalIT Jobs (Inteligência de Mercado)

Como rodar:
    pip install -r requirements.txt
    streamlit run app.py
"""

import pandas as pd
import plotly.express as px
import streamlit as st

import firestore_data as fdb

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO GERAL
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="TI Sem Fronteiras",
    page_icon="🌐",
    layout="wide",
)

CORES = {
    "primaria": "#2563EB",
    "secundaria": "#0F172A",
    "destaque": "#22C55E",
}

df_paises = pd.DataFrame(fdb.carregar_paises())
df_vagas = pd.DataFrame(fdb.carregar_vagas())
df_radar = pd.DataFrame(fdb.carregar_radar_tecnologias())
TRILHAS_QUALIFICACAO = fdb.carregar_trilhas_qualificacao()


# ---------------------------------------------------------------------------
# SIDEBAR - NAVEGAÇÃO
# ---------------------------------------------------------------------------
st.sidebar.title("🌐 TI Sem Fronteiras")
st.sidebar.caption("SIRITEC · IFS Campus Socorro")
pagina = st.sidebar.radio(
    "Navegação",
    ["🏠 Início", "🗺️ MundoDev", "💼 GlobalIT Jobs"],
)
st.sidebar.markdown("---")
modo = fdb.modo_dados()
if modo == "firestore":
    st.sidebar.success("🔥 Conectado ao Firestore (Firebase)")
else:
    st.sidebar.info("📦 Usando dados locais de demonstração (Firebase não conectado)")
st.sidebar.caption(
    "Protótipo acadêmico. Em versão futura, os dados virão de APIs reais e raspagem de dados."
)


# ---------------------------------------------------------------------------
# PÁGINA: INÍCIO
# ---------------------------------------------------------------------------
def pagina_inicio():
    st.title("TI Sem Fronteiras")
    st.subheader("Ecossistema unificado para internacionalização de carreiras em TI")

    st.markdown(
        """
        O projeto **TI Sem Fronteiras** nasce para eliminar barreiras geográficas para o
        talento técnico do Instituto Federal de Sergipe, tratando a carreira internacional
        como um processo de duas etapas: **a escolha do destino** e **a conquista da vaga**.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🗺️ Módulo I — MundoDev")
        st.markdown(
            "**Inteligência Geográfica.** Mapeamento de países, cultura, custo de vida "
            "e requisitos de imigração."
        )
        st.markdown(
            "- Mapeamento de países\n"
            "- Guia de sobrevivência (custo de vida, moradia, saúde)\n"
            "- Segurança jurídica (vistos e regularização)"
        )
    with col2:
        st.markdown("### 💼 Módulo II — GlobalIT Jobs")
        st.markdown(
            "**Inteligência de Mercado.** Oportunidades de trabalho, tecnologias "
            "demandadas e requisitos técnicos."
        )
        st.markdown(
            "- Monitoramento de vagas\n"
            "- Radar de tecnologias\n"
            "- Trilhas de qualificação"
        )

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Países mapeados", len(df_paises))
    c2.metric("Vagas monitoradas", len(df_vagas))
    c3.metric("Tecnologias no radar", len(df_radar))


# ---------------------------------------------------------------------------
# PÁGINA: MUNDODEV
# ---------------------------------------------------------------------------
def pagina_mundodev():
    st.title("🗺️ MundoDev")
    st.caption("Módulo I — Inteligência Geográfica")

    regioes = ["Todas"] + sorted(df_paises["regiao"].unique().tolist())
    regiao_sel = st.selectbox("Filtrar por região", regioes)

    df_filtrado = df_paises if regiao_sel == "Todas" else df_paises[df_paises["regiao"] == regiao_sel]

    fig = px.bar(
        df_filtrado.sort_values("salario_medio_ti_usd"),
        x="salario_medio_ti_usd",
        y="pais",
        orientation="h",
        color="demanda_ti",
        title="Salário médio em TI por país (USD/mês, estimado)",
        labels={"salario_medio_ti_usd": "Salário médio (USD)", "pais": "País", "demanda_ti": "Demanda em TI"},
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Ficha por país")
    pais_sel = st.selectbox("Escolha um país para ver detalhes", df_filtrado["pais"].tolist())
    dados = df_paises[df_paises["pais"] == pais_sel].iloc[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Custo de vida (USD/mês)", f"${dados['custo_vida_mensal_usd']:,}")
    col2.metric("Salário médio TI (USD/mês)", f"${dados['salario_medio_ti_usd']:,}")
    col3.metric("Demanda em TI", dados["demanda_ti"])

    st.markdown(f"**Idioma:** {dados['idioma']}")
    st.markdown(f"**Visto recomendado:** {dados['visto']} · *Dificuldade: {dados['dificuldade_visto']}*")
    st.markdown(f"**Resumo:** {dados['resumo']}")


# ---------------------------------------------------------------------------
# PÁGINA: GLOBALIT JOBS
# ---------------------------------------------------------------------------
def pagina_globalit_jobs():
    st.title("💼 GlobalIT Jobs")
    st.caption("Módulo II — Inteligência de Mercado")

    tab1, tab2, tab3 = st.tabs(["📋 Vagas", "📡 Radar de Tecnologias", "🎯 Trilhas de Qualificação"])

    # --- Vagas ---
    with tab1:
        col_f1, col_f2, col_f3 = st.columns(3)
        paises_opt = ["Todos"] + sorted(df_vagas["pais"].unique().tolist())
        senioridade_opt = ["Todas"] + sorted(df_vagas["senioridade"].unique().tolist())
        modalidade_opt = ["Todas"] + sorted(df_vagas["modalidade"].unique().tolist())

        pais_f = col_f1.selectbox("País", paises_opt)
        senioridade_f = col_f2.selectbox("Senioridade", senioridade_opt)
        modalidade_f = col_f3.selectbox("Modalidade", modalidade_opt)

        df_v = df_vagas.copy()
        if pais_f != "Todos":
            df_v = df_v[df_v["pais"] == pais_f]
        if senioridade_f != "Todas":
            df_v = df_v[df_v["senioridade"] == senioridade_f]
        if modalidade_f != "Todas":
            df_v = df_v[df_v["modalidade"] == modalidade_f]

        st.write(f"**{len(df_v)} vaga(s) encontrada(s)**")
        for _, vaga in df_v.iterrows():
            with st.container(border=True):
                st.markdown(f"#### {vaga['titulo']} — {vaga['empresa']}")
                st.markdown(
                    f"📍 {vaga['pais']} · 🏷️ {vaga['modalidade']} · 🎓 {vaga['senioridade']} "
                    f"· 💰 USD {vaga['salario_faixa_usd']}/mês"
                )
                st.markdown("**Stack:** " + ", ".join(vaga["stack"]))

    # --- Radar de tecnologias ---
    with tab2:
        fig_radar = px.bar(
            df_radar.sort_values("demanda"),
            x="demanda",
            y="tecnologia",
            color="categoria",
            orientation="h",
            title="Radar de tecnologias mais demandadas no exterior",
            labels={"demanda": "Índice de demanda (0-100)", "tecnologia": "Tecnologia"},
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # --- Trilhas de qualificação ---
    with tab3:
        for trilha in TRILHAS_QUALIFICACAO:
            with st.expander(f"🎯 {trilha['area']} — {trilha['competencia']}"):
                for cert in trilha["certificacoes"]:
                    st.checkbox(cert, key=f"{trilha['area']}-{cert}")


# ---------------------------------------------------------------------------
# ROTEAMENTO
# ---------------------------------------------------------------------------
if pagina == "🏠 Início":
    pagina_inicio()
elif pagina == "🗺️ MundoDev":
    pagina_mundodev()
elif pagina == "💼 GlobalIT Jobs":
    pagina_globalit_jobs()
