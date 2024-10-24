import streamlit as st
import pandas as pd
import plotly.express as px

df_aux = pd.read_csv('data/finbraRREOgeral.csv')

cidades_novas = ['Tamandaré - PE', 'Barra de São Miguel - AL', 'Cabo Frio - RJ', 'Niterói - RJ', 'Ilhéus - BA']
regex = '|'.join(cidades_novas)
df_cidades_novas = df_aux[df_aux['Instituição'].str.contains(regex, case=False, na=False)]

df_cidades_novas['Valor'] = df_cidades_novas['Valor'].str.replace(',', '.').astype(float)

df_cidades_novas = df_cidades_novas.groupby(['Instituição', 'Conta', 'Ano', 'UF']).agg({'Valor': 'sum', 'População': 'mean'}).reset_index()


df = pd.read_csv('outputs/df_state.csv')
df['Valor'] = df['Valor'].astype(float)


df = pd.concat([df, df_cidades_novas])

# Converter a coluna 'Valor' para numérica
#df['Valor'] = df['Valor'].astype(float)

# Definir as contas de interesse (ICMS e IPVA)
tributos_interesse = ['Cota-Parte do ICMS', 'Cota-Parte do IPVA']

# Adicionar um seletor de múltiplos estados (UFs)
ufs_selecionados = st.sidebar.multiselect('Selecione os estados (UF)', df['UF'].unique())

# Filtrar os dados para os estados selecionados e as contas de ICMS e IPVA
if ufs_selecionados:
    df_filtrado = df[(df['Conta'].isin(tributos_interesse)) & (df['UF'].isin(ufs_selecionados))]
else:
    df_filtrado = df[df['Conta'].isin(tributos_interesse)]

# Exibir soma total dos valores para os estados selecionados
for tributo in tributos_interesse:
    df_tributo = df_filtrado[df_filtrado['Conta'] == tributo]
    soma_valores = df_tributo['Valor'].sum()
    
    
    # Gráfico interativo por estado e ano
    fig = px.line(df_tributo, x='Ano', y='Valor', color='Instituição',
                  title=f'Valores de {tributo} por Ano e Cidade')
    
    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)
    st.write(f'Soma total de {tributo} para os estados selecionados: R$ {soma_valores:,.2f}')
