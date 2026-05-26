import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Escala Mensal",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide all Streamlit chrome so the app fills the full viewport
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; height: 0; }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    section[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

html = Path("calendario.html").read_text(encoding="utf-8")
components.html(html, height=950, scrolling=True)
