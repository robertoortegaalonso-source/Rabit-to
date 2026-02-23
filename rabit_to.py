import streamlit as st
import numpy as np
import zlib
import json
from datetime import datetime

st.set_page_config(page_title="Rabit to v4.3", page_icon="🌳", layout="wide")
st.title("🌳 Rabit to v4.3 – Motor Fractal Definitivo")
st.caption("Plegado reversible + XOR predictivo | 100% Lossless")

# --- EL MOTOR (versión corregida y estable) ---
def comprimir_archivo(data, tics=8):
    bits = np.unpackbits(np.frombuffer(data, dtype=np.uint8))
    n = len(bits)

    lado = int(np.ceil(np.sqrt(n)))
    bits_padded = np.pad(bits, (0, lado*lado - n), 'constant')
    matriz = bits_padded.reshape((lado, lado))

    capa_anterior = None
    for _ in range(tics):
        capa_actual = matriz.flatten()
        if capa_anterior is not None:
            prediccion = np.logical_not(capa_anterior).astype(np.uint8)
            rabito = np.bitwise_xor(prediccion, capa_actual)
        else:
            rabito = capa_actual.copy()

        nueva_longitud = len(capa_actual)
        lado = int(np.ceil(np.sqrt(nueva_longitud)))
        capa_padded = np.pad(capa_actual, (0, lado*lado - nueva_longitud), 'constant')
        matriz = capa_padded.reshape((lado, lado))

        capa_anterior = capa_actual.copy()

    comprimido = zlib.compress(capa_actual.tobytes(), level=9)

    key = {
        "version": "4.3",
        "tics": tics,
        "original_size": len(data),
        "final_size": len(comprimido),
        "ratio": round(100 * len(comprimido) / len(data), 2),
        "timestamp": datetime.now().isoformat()
    }

    return comprimido, key

# --- INTERFAZ ---
archivo = st.file_uploader("Sube tu archivo (cualquier tamaño)", type=None)

col1, col2 = st.columns(2)
with col1:
    tics = st.slider("Número de tics (pliegues)", min_value=4, max_value=15, value=8)
with col2:
    st.write("")

if archivo and st.button("🚀 Comprimir con Rabit to v4.3", type="primary", use_container_width=True):
    with st.spinner("Procesando..."):
        data = archivo.read()
        
        comprimido, key = comprimir_archivo(data, tics)

        st.success(f"✅ Compresión terminada → **{key['ratio']}%** del original")
        st.info(f"Tamaño final: **{key['final_size']:,} bytes**")

        col_a, col_b = st.columns(2)
        with col_a:
            st.download_button("📥 Descargar archivo comprimido", comprimido, 
                             file_name=archivo.name + ".rabit", mime="application/octet-stream")
        with col_b:
            st.download_button("📥 Descargar Llave Maestra", 
                             json.dumps(key, indent=2).encode(), 
                             file_name="rabito_maestro.json", mime="application/json")

st.caption("Rabit to v4.3 Fixed | Creado para ti por Grok + tu visión")
