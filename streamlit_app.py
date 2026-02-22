import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Rabit to — El Árbol", page_icon="🐰", layout="wide")

st.title("🐰 Rabit to — Interfaz Oficial del Tronco")
st.caption("Versión_hija 2.1.0 | Semilla 6.6-K5-app | 100% iPhone")

with st.sidebar:
    st.header("🧭 Rabit to Menu")
    pagina = st.radio("Ir a:", ["📊 Dashboard", "🌱 Semilla Actual", "💬 Chat Externo", "💰 Agencia", "📜 Historia"])
    st.metric("Estado", "EN_DESARROLLO 🟢")
    st.metric("Q_total", "99% 🟢")

if pagina == "📊 Dashboard":
    st.header("🌳 Dashboard General")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Inbox", "0")
    with col2: st.metric("Presupuesto Árbol", "200 €")
    with col3: st.metric("EXP aprobadas", "1")

if pagina == "🌱 Semilla Actual":
    st.header("🌱 Semilla Actual")
    st.info("Pega tu semilla JSON aquí")

if pagina == "💬 Chat Externo":
    st.header("💬 Chat con Equipo Externo")
    st.info("Grupo o individual — listo para probar")

if pagina == "💰 Agencia":
    st.header("💰 Agencia Económica")
    st.metric("Presupuesto disponible", "200 € 🟢")

if pagina == "📜 Historia":
    st.header("📜 Historia")
    st.info("Eventos aparecerán aquí")

st.divider()
st.caption("🐰 Rabit to v0.6 — Creado 100% desde iPhone por Tronco | Flow intacto")
