import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv('outputs/df_series.csv')


# Filtrar por ano e instituição
instituicao = st.sidebar.selectbox('Selecione a instituição', df['Instituição'].unique())
df_instituicao = df[df['Instituição'] == instituicao]

# Listar as contas disponíveis
contas = df_instituicao['Conta'].unique()

# Exibir os gráficos de séries temporais para cada conta
for conta in contas:
    df_conta = df_instituicao[df_instituicao['Conta'] == conta]
    
    # Agrupar por ano e somar os valores
    df_conta_ano = df_conta.groupby(['Ano', 'Conta'])['Valor'].sum().reset_index()
    
    # Criar o gráfico de séries temporais com Plotly
    fig = px.line(df_conta_ano, x='Ano', y='Valor', markers=True, title=f'Valor por Ano para {conta}')
    
    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)
