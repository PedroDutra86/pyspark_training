import streamlit as st
import pandas as pd
import numpy as np
# Carregar os dados


def load_data():
    data = pd.read_csv('netflix_titles.csv')  # Substitua pelo seu arquivo
    return data
data = load_data()
# Título
st.title("Análise de Dados")
# Mostrar os dados
if st.checkbox('Mostrar dados'):
    st.write(data)
# Análise simples
st.subheader("Estatísticas descritivas")
st.write(data.describe())
# Gráficos
st.subheader("Gráfico de dispersão")
x_axis = st.selectbox("Escolha a variável do eixo X", data.columns)
y_axis = st.selectbox("Escolha a variável do eixo Y", data.columns)
st.write("Gráfico de dispersão entre", x_axis, "e", y_axis)
st.scatter_chart(data[[x_axis, y_axis]])
# Adicione mais análises conforme necessário