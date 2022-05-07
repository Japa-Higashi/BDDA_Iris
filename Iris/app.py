import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

st.write("# Classificação da Íris")
st.write("## Exemplo de complemento de pétala e sépala")
st.sidebar.write("### Parametros")
st.sidebar.slider("Comprimento da sépala", 4.8, 8.0, 5.8, 0.1)
st.sidebar.slider("Com primento da pétala", 0.9, 7.0, 3.8, 0.1)

with open("objetos.pkl", "rb") as arquivo:
  ss, dtc = pickle.load(arquivo)
