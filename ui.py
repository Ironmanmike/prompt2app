import streamlit as st
import os
from main import generate_app_code

st.set_page_config(page_title="Espriton AI - Prompt2App", layout="wide")
st.title("🚀 Espriton AI — Prompt to App Generator")

prompt = st.text_area("Describe the app you want to build:", height=200)

if st.button("Generate App Code"):
    if prompt.strip():
        with st.spinner("Generating app..."):
            result = generate_app_code(prompt)
            st.code(result, language="python")
    else:
        st.warning("Please enter a prompt first.")
