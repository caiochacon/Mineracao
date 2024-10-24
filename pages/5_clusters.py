import streamlit as st
import pandas as pd
import plotly.graph_objs as go


pivot_df = pd.read_csv('outputs/pivot_df.csv')
df_pca = pd.read_csv('outputs/df_pca.csv')

pivot_df.columns = ['_'.join(map(str, col)) if isinstance(col, tuple) else col for col in pivot_df.columns]

df = pivot_df.merge(df_pca[['PC1', 'PC2', 'Instituição']], left_on='Instituição', right_on='Instituição', how='left')

# Plota o gráfico de dispersão com Plotly
st.write("### Gráfico para os Clusters")

scatter = go.Scatter(
    x=df['PC1'],
    y=df['PC2'],
    mode='markers',  # 'markers' para pontos, 'lines' para linhas, 'lines+markers' para ambos
    marker=dict(size=10, color=df['Cluster_KMeans']),
    text=df['Cluster_KMeans'],
    name='Scatterplot com Kmeans'
)
# Criação da figura com o traço do scatterplot
fig = go.Figure(data=[scatter])
# Configuração do layout do gráfico
fig.update_layout(
    title='Clsuterização com KMeans',
    xaxis_title='PCA 1',
    yaxis_title='PCA 2'
)
# Exibe o gráfico no Streamlit
st.plotly_chart(fig)


scatter = go.Scatter(
    x=df['PC1'],
    y=df['PC2'],
    mode='markers',  # 'markers' para pontos, 'lines' para linhas, 'lines+markers' para ambos
    marker=dict(size=10, color=df['Cluster_DIANA']),
    text=df['Cluster_DIANA'],
    name='Scatterplot com DIANA'
)
# Criação da figura com o traço do scatterplot
fig = go.Figure(data=[scatter])
# Configuração do layout do gráfico
fig.update_layout(
    title='Clsuterização com DIANA',
    xaxis_title='PCA 1',
    yaxis_title='PCA 2'
)
# Exibe o gráfico no Streamlit
st.plotly_chart(fig)


scatter = go.Scatter(
    x=df['PC1'],
    y=df['PC2'],
    mode='markers',  # 'markers' para pontos, 'lines' para linhas, 'lines+markers' para ambos
    marker=dict(size=10, color=df['Cluster_AGNES']),
    text=df['Cluster_AGNES'],
    name='Scatterplot com AGNES'
)
# Criação da figura com o traço do scatterplot
fig = go.Figure(data=[scatter])
# Configuração do layout do gráfico
fig.update_layout(
    title='Clsuterização com AGNES',
    xaxis_title='PCA 1',
    yaxis_title='PCA 2'
)
# Exibe o gráfico no Streamlit
st.plotly_chart(fig)

# Exibe a tabela no Streamlit
st.write("### Tabela de Cidades, Valores por Ano e Clusters")
st.dataframe(df[['PC1', 'PC2', 'Instituição', 'Cluster_KMeans', 'Cluster_DIANA', 'Cluster_AGNES']])