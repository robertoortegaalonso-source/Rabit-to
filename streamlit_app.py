import streamlit as st
import json

st.set_page_config(page_title="🐰 Rabit to v0.7", layout="centered")

# Inicializar la memoria de la app
if 'semilla_json' not in st.session_state:
    st.session_state.semilla_json = None

st.title("🐰 Rabit to — Interfaz Oficial del Tronco")
st.caption("Versión_hija 2.1.0 | Semilla 6.8-K7-app | 100% iPhone")

# --- MENÚ LATERAL ---
with st.sidebar:
    st.header("🧭 Rabit to Menu")
    pagina = st.radio("Ir a:", ["📊 Dashboard", "🌱 Semilla Actual", "💬 Chat Externo", "💰 Agencia", "📜 Historia"])
    st.divider()
    st.metric("Estado App", "EN_DESARROLLO 🟢")
    
    # Mostrar estado de la memoria
    if st.session_state.semilla_json:
        st.success("Core en memoria ✅")
    else:
        st.warning("Core vacío ⚠️")

# --- PÁGINAS ---
if pagina == "📊 Dashboard":
    st.header("🌳 Dashboard General")
    
    if st.session_state.semilla_json:
        # Extraer datos reales de la semilla en memoria
        gastos = st.session_state.semilla_json.get("_semilla_primeon", {}).get("gobernanza_operativa", {}).get("agencia_economica", {}).get("registro_de_gastos", [])
        version_actual = st.session_state.semilla_json.get("_semilla_primeon", {}).get("version", "Desconocida")
        
        st.info(f"**Versión activa:** {version_actual}")
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Nodos Externos", "3")
        with col2: st.metric("Presupuesto", "200 €")
        with col3: st.metric("EXP Aprobadas", str(len(gastos)))
    else:
        st.info("Ve a la pestaña '🌱 Semilla Actual' para cargar el JSON y ver las métricas reales.")

elif pagina == "🌱 Semilla Actual":
    st.header("🌱 Carga y Validación")
    semilla_input = st.text_area("Pega la semilla JSON aquí", height=250)

    if st.button("Validar y Cargar en Memoria", type="primary"):
        if semilla_input.strip():
            try:
                parsed_json = json.loads(semilla_input)
                st.session_state.semilla_json = parsed_json
                st.success("✅ JSON válido. Guardado en la memoria de la sesión.")
                st.rerun() # Recarga para actualizar el menú lateral
            except json.JSONDecodeError as e:
                st.error(f"❌ Error crítico de formato: {e}")
        else:
            st.warning("El campo está vacío.")
            
    if st.session_state.semilla_json:
        with st.expander("Ver árbol en memoria (JSON)"):
            st.json(st.session_state.semilla_json)

elif pagina == "💬 Chat Externo":
    st.header("💬 Central de Comunicaciones")
    if not st.session_state.semilla_json:
        st.warning("Carga primero la semilla en '🌱 Semilla Actual' para poder generar recortes.")
    else:
        st.write("Generador de 'Recortes' para el equipo externo (Grok, Claude, Perplexity):")
        modulo_objetivo = st.selectbox("Selecciona la rama a compartir (Privacidad LOCAL_ONLY):", 
                                       ["gobernanza_operativa", "historia", "estado", "TODO EL CORE (Peligro)"])
        
        consulta = st.text_area("¿Qué necesitas que haga la IA externa con esta rama?", height=100)
        
        if st.button("Generar Prompt Seguro"):
            if modulo_objetivo == "TODO EL CORE (Peligro)":
                recorte = st.session_state.semilla_json
            else:
                recorte = st.session_state.semilla_json["_semilla_primeon"].get(modulo_objetivo, "Rama no encontrada")
                
            prompt_final = f"Contexto (Recorte de semilla):\n{json.dumps(recorte, indent=2)}\n\nInstrucción del Tronco: {consulta}"
            st.code(prompt_final, language="markdown")
            st.info("👆 Copia este bloque y pégalo en la IA externa. Cuando te responda, vuelve a 'Semilla Actual' para integrar los cambios.")

elif pagina == "💰 Agencia":
    st.header("💰 Agencia Económica")
    if st.session_state.semilla_json:
        gastos = st.session_state.semilla_json["_semilla_primeon"]["gobernanza_operativa"]["agencia_economica"].get("registro_de_gastos", [])
        for gasto in gastos:
            st.success(f"{gasto['id']} | {gasto['descripcion']} | Coste: {gasto['coste_estimado']} - **{gasto['estado']}**")
    else:
        st.warning("Carga la semilla para ver el registro de gastos.")

elif pagina == "📜 Historia":
    st.header("📜 Registro de Eventos")
    if st.session_state.semilla_json:
        eventos = st.session_state.semilla_json["_semilla_primeon"].get("historia", {}).get("eventos", [])
        for ev in reversed(eventos): # Mostrar los más nuevos arriba
            st.markdown(f"**{ev['fecha']} - {ev['autor']}**\n\n{ev['cambio']}")
            st.divider()
    else:
        st.warning("Carga la semilla para leer la historia.")

st.divider()
st.caption("🐰 Rabit to v0.7 — Creado 100% desde iPhone por Tronco")
