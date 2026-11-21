from pathlib import Path

import pandas as pd
import streamlit as st

CARPETA_DATOS = Path(__file__).resolve().parent.parent / "data"

st.set_page_config(page_title="Análisis de libros", page_icon="📚", layout="wide")
