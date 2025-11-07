# 🦷 Editor de Tarifario — Streamlit Cloud

Aplicación web en **Streamlit** para visualizar, editar y actualizar un archivo Excel con múltiples hojas (clientes/empresas).

## 🚀 Características
- Carga archivos Excel (.xlsx)
- Muestra todas las hojas del libro
- Permite **editar**, **agregar** y **eliminar** filas o columnas
- Descarga el archivo actualizado
- 100% funcional en la nube con **Streamlit Cloud**

## 📦 Instalación local (opcional)
```bash
pip install streamlit pandas openpyxl
streamlit run streamlit_tarifario_cloud.py
```

## 🌐 Despliegue en Streamlit Cloud
1. Sube estos archivos a un nuevo repositorio de GitHub:
   - `streamlit_tarifario_cloud.py`
   - `requirements.txt`
   - `README.md`
2. Ve a [Streamlit Cloud](https://streamlit.io/cloud) → **New app**
3. Conecta tu cuenta de GitHub
4. Elige el repositorio y escribe:
   ```
   streamlit_tarifario_cloud.py
   ```
5. Haz clic en **Deploy** 🚀

Tu app estará disponible en línea en unos segundos.

## 📊 Uso
1. Sube tu archivo **TARIFARIO 2025 ODOO copia.xlsx**
2. Selecciona la hoja (empresa/cliente)
3. Edita, agrega o elimina filas
4. Descarga el Excel actualizado

---

Hecho con ❤️ en Streamlit
