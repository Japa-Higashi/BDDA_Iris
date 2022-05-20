import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write("# Classificação de Diagnostico de Cancer")
st.write("## Exemplo com radius2 e concavity2")
st.sidebar.write("### Parâmetros")
radius2 = st.sidebar.slider("Comprimento da radius2", -2.0, 2.0,0.2,0.1)
concavity2 = st.sidebar.slider("Comprimento da concavity2",-2.0, 2.0, 0.2, 0.1)

with open("objetos.pkl", "rb") as arquivo:
  ss, dtc = pickle.load(arquivo)
  
estrutura = {'radius2' : radius2, 'concavity2' : concavity2}

df = pd.DataFrame(estrutura, index = [0]) 
st.write("### Parâmetros de entreada")
st.write(df)

df = ss.transform(df)
st.write(df)

predicao = dtc.predict(df)
st.write(f"A chance de ter cancer é : {predicao[0]}")
predicao = dtc.predict_proba(df)
predicao = pd.DataFrame(predicao)
predicao.rename({
  0: "B",
  1: "M"
}, axis = 1, inplace = True)

st.write("Probabilidade")
st.write(predicao)
