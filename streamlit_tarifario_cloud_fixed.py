import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Tarifario — Editor Web", layout="wide")
st.title("Editor de Tarifario (Subible a Streamlit Cloud)")
st.markdown("App ligera para subir, editar y descargar un archivo Excel con múltiples hojas (empresas/clientes). Interfaz en español.")

@st.cache_data()
def read_excel_bytes(file_bytes: bytes):
    with BytesIO(file_bytes) as b:
        xls = pd.ExcelFile(b)
        sheets = {name: xls.parse(name) for name in xls.sheet_names}
    return sheets

def to_excel_bytes(sheets: dict) -> bytes:
    out = BytesIO()
    with pd.ExcelWriter(out, engine="openpyxl") as writer:
        for name, df in sheets.items():
            safe_name = str(name)[:31]
            df.to_excel(writer, sheet_name=safe_name, index=False)
    out.seek(0)
    return out.read()

st.sidebar.header("Carga de archivo")
uploaded = st.sidebar.file_uploader("Sube tu archivo Excel (.xlsx)", type=["xlsx"], accept_multiple_files=False)

if uploaded is None:
    st.info("Sube el archivo Excel para comenzar.")
    st.stop()

bytes_data = uploaded.read()
sheets = read_excel_bytes(bytes_data)
sheet_names = list(sheets.keys())
selected = st.sidebar.selectbox("Selecciona la hoja / cliente", sheet_names)

df = sheets[selected].copy()
st.subheader(f"Hoja: {selected}")
st.write(f"Filas: {df.shape[0]}  —  Columnas: {df.shape[1]}")

edited = st.data_editor(df, num_rows="dynamic")
sheets[selected] = edited

excel_bytes = to_excel_bytes(sheets)
st.download_button(label="Descargar archivo Excel (.xlsx)",
                   data=excel_bytes,
                   file_name=f"tarifario_actualizado_{uploaded.name}",
                   mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

st.caption("App Streamlit Cloud — Editor de Tarifario 2025")