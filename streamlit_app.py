import streamlit as st
import json

st.set_page_config(page_title="🐰 Rabit to v0.6", layout="centered")

st.title("🐰 Rabit to — Interfaz Oficial del Tronco")
st.caption("Versión_hija 2.1.0 | Semilla 6.7-K6-app | 100% iPhone")

# --- MENÚ LATERAL ---
with st.sidebar:
    st.header("🧭 Rabit to Menu")
    pagina = st.radio("Ir a:", ["📊 Dashboard", "🌱 Semilla Actual", "💬 Chat Externo", "💰 Agencia", "📜 Historia"])
    st.divider()
    st.metric("Estado App", "EN_DESARROLLO 🟢")
    st.metric("Q_total", "99% 🟢")

# --- PÁGINAS ---
if pagina == "📊 Dashboard":
    st.header("🌳 Dashboard General")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Inbox", "0")
    with col2: st.metric("Presupuesto Árbol", "200 €")
    with col3: st.metric("EXP Aprobadas", "1")
    
    st.divider()
    st.info("Ve a la pestaña '🌱 Semilla Actual' para cargar el JSON y habilitar el validador del núcleo.")

elif pagina == "🌱 Semilla Actual":
    st.header("🌱 Carga y Validación")
    semilla_input = st.text_area("Pega la semilla JSON (versión 6.7-K6-app) aquí", height=300)

    if st.button("Validar y Cargar Semilla", type="primary"):
        if semilla_input.strip():
            try:
                # Validador de seguridad
                semilla_json = json.loads(semilla_input)
                st.success("✅ JSON válido. Core intacto y cargado.")
                
                # Extraer datos de la semilla en vivo
                if "_semilla_primeon" in semilla_json:
                    version = semilla_json["_semilla_primeon"].get("version", "Desconocida")
                    estado = semilla_json["_semilla_primeon"].get("estado", "Desconocido")
                    st.info(f"**Versión detectada:** {version} | **Estado:** {estado}")
                
                with st.expander("Ver árbol completo (JSON)"):
                    st.json(semilla_json)
                    
            except json.JSONDecodeError as e:
                st.error(f"❌ Error crítico de formato: {e}")
                st.warning("Revisa comas sueltas o llaves sin cerrar en el JSON. Guardado bloqueado por seguridad.")
        else:
            st.warning("El campo está vacío. Pega una semilla primero.")

elif pagina == "💬 Chat Externo":
    st.header("💬 Equipo Externo")
    st.info("Página en construcción. Aquí irán las plantillas para Grok, Claude y Perplexity.")

elif pagina == "💰 Agencia":
    st.header("💰 Agencia Económica")
    st.success("EXP-2.1.0-2026-02-22-001: Despliegue Streamlit Cloud (0 EUR) - **APROBADO**")

elif pagina == "📜 Historia":
    st.header("📜 Registro de Eventos")
    st.info("Historial bloqueado. Carga una semilla válida primero para ver los eventos.")

st.divider()
st.caption("🐰 Rabit to v0.6 — Creado 100% desde iPhone por Tronco | Flow intacto")
