import streamlit as st
import pandas as pd

dados = {
    'nome': ['Pedro', 'Mauro', 'Josue'],
    'idade': [24, 55, 32]
}
df = pd.DataFrame(dados)

st.bar_chart(dados, x = 'nome', y = 'idade')