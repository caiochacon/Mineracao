import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv('outputs/df1.csv')

# Exibir um gráfico de exemplo no Streamlit
st.title("Dashboard de Impostos por Município/Ano")

# Filtrar por ano
ano = st.sidebar.selectbox('Selecione o ano', df['Ano'].unique())

# Filtrar por instituição
instituicao = st.sidebar.selectbox('Selecione a instituição', df['Instituição'].unique())

# Dados filtrados
df_filtrado = df[(df['Ano'] == ano) & (df['Instituição'] == instituicao)]

# Criar gráfico
fig = px.bar(df_filtrado, x='Conta', y='Valor', title=f'Valores por Conta para {instituicao} no ano {ano}')

# Mostrar gráfico no Streamlit usando Plotly
st.plotly_chart(fig)