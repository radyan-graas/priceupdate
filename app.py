import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PriceSync",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit chrome so the app feels standalone
st.markdown("""
    <style>
    #MainMenu { visibility: hidden; }
    footer    { visibility: hidden; }
    header    { visibility: hidden; }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

with open("pricesync.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=960, scrolling=True)
