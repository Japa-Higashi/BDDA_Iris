
import streamlit as st

st.write("# Classificação da Íris")
st.write("## Exemplo de complemento de pétala e sépala")
st.sidebar.write("### Parametros")
st.sidebar.slider("Comprimento da sépala", 4.8, 8.0, 5.8, 0.1)
st.sidebar.slider("Com primento da pétala", 0.9, 7.0, 3.8, 0.1)
