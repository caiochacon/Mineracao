import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('data/finbraRREOgeral.csv')

# Converter a coluna 'Valor' para numérica (removendo vírgulas)
df['Valor'] = df['Valor'].str.replace(',', '').astype(float)

# Filtrar dados e realizar agrupamento
df = df.groupby(['Instituição', 'Conta', 'Ano']).agg({'Valor': 'sum', 'População': 'mean'}).reset_index()

# Exibir um gráfico de exemplo no Streamlit
st.title("Dashboard de Análise Financeira")

# Filtrar por ano
ano = st.sidebar.selectbox('Selecione o ano', df['Ano'].unique())

# Filtrar por instituição
instituicao = st.sidebar.selectbox('Selecione a instituição', df['Instituição'].unique())

# Dados filtrados
df_filtrado = df[(df['Ano'] == ano) & (df['Instituição'] == instituicao)]

# Criar gráfico
fig, ax = plt.subplots()
ax.bar(df_filtrado['Conta'], df_filtrado['Valor'])
ax.set_title(f'Valores por Conta para {instituicao} no ano {ano}')
ax.set_ylabel('Valor')
ax.set_xlabel('Conta')

# Mostrar gráfico no Streamlit
st.pyplot(fig)