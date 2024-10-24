import streamlit as st
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('outputs/df_previsao.csv')

# Filtro de instituição
instituicoes = df['Instituição'].unique()
instituicao_selecionada = st.sidebar.selectbox("Selecione a Instituição", instituicoes)

# Filtra os dados pela instituição selecionada
df_filtrado = df[df['Instituição'] == instituicao_selecionada]

# Cria o gráfico de série temporal com Plotly

for conta in df_filtrado['Conta'].unique():
    df_conta = df_filtrado[df_filtrado['Conta'] == conta]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_conta['Ano'][:7], 
        y=df_conta['Valor'][:7], 
        mode='lines+markers', 
        name=f"Valores originais: {conta}",
        line=dict(color='red')
    ))
    
    fig.add_trace(go.Scatter(
        x=df_conta['Ano'][7:], 
        y=df_conta['Valor'][7:], 
        mode='lines+markers', 
        name=f'Previsão {conta}',
        line=dict(color='blue', dash='dash')
    ))

    # Configurações do layout do gráfico
    fig.update_layout(
        title=f'Série Temporal com Previsão de {conta}',
        xaxis_title='Ano',
        yaxis_title='Valor',
        legend_title='Legenda: '
    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)