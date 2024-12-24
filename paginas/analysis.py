import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import globals
import graficos

tab1, tab2 = st.tabs(['Análise Exploratória', 'Gráficos'])

with tab1:
    cbAno = st.selectbox('Selecione o Ano:', list(globals.lAno.keys()), key = "cbAno")

    df_ano = globals.df    
    if(cbAno != 'Todos'):
        df_ano = globals.df[globals.df['ANO'] == globals.lAno[cbAno]]
        if(globals.lAno[cbAno] > 2020):
            df_ano_anterior = globals.df[globals.df['ANO'] == globals.lAno[cbAno]-1]

    num_colunas_pedras = len(globals.lPedras)
    colunas_2 = st.columns(num_colunas_pedras, border=True)
    for i, dados in enumerate(globals.lPedras):
        coluna_atual = colunas_2[i % num_colunas_pedras]
        with coluna_atual:
            if(cbAno != 'Todos' and globals.lAno[cbAno] > 2020):
                st.metric(dados, label_visibility='visible', help='Comparativo em relação ao ano anterior', value=np.sum(df_ano['PEDRA'] == dados), delta= int(np.sum(df_ano['PEDRA'] == dados) - np.sum(df_ano_anterior['PEDRA'] == dados)))
            else:
                st.metric(dados, np.sum(df_ano['PEDRA'] == dados), delta=None)            

    num_colunas = len(globals.lIndicadores_1)
    colunas_1 = st.columns(num_colunas, border=True)

    for i, dados in enumerate(globals.lIndicadores_1):
        coluna_atual = colunas_1[i % num_colunas]
        with coluna_atual:
            st.subheader(dados, help='Comparativo em relação ao ano anterior')
            if(cbAno != 'Todos' and globals.lAno[cbAno] > 2020):
                st.metric('Média:', df_ano[dados].mean().round(2), border=False, delta=round(df_ano[dados].mean().round(2) - df_ano_anterior[dados].mean().round(2),2))
                st.metric('Mediana:', df_ano[dados].median().round(2), border=False, delta=round(df_ano[dados].median().round(2) - df_ano_anterior[dados].median().round(2),2))
                st.metric('Min:', df_ano[dados].min().round(2), border=False, delta=round(df_ano[dados].min().round(2) - df_ano_anterior[dados].min().round(2),2))
                st.metric('Max:', df_ano[dados].max().round(2), border=False, delta=round(df_ano[dados].max().round(2) - df_ano_anterior[dados].max().round(2), 2))
            else:
                st.metric('Média:', df_ano[dados].mean().round(2),border=False, delta=None, delta_color='off')
                st.metric('Mediana:', df_ano[dados].median().round(2),border=False, delta=None, delta_color='off')
                st.metric('Min:', df_ano[dados].min().round(2),border=False, delta=None, delta_color='off')
                st.metric('Max:', df_ano[dados].max().round(2),border=False, delta=None, delta_color='off')

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        cbAno_grafico = st.selectbox('Selecione o Ano:', list(globals.lAno.keys()), key = "cbAno_grafico")
    with col2:
        cbIndicador = st.selectbox('Selecione o Indicador:', globals.lIndicadores_1[1:], key = "cbIndicador")

    df_ano_grafico = globals.df    
    if(cbAno_grafico != 'Todos'):
        df_ano_grafico = globals.df[globals.df['ANO'] == globals.lAno[cbAno_grafico]]       

    st.plotly_chart(graficos.scatterChart(df_ano_grafico, 'INDE', cbIndicador, 'Relação de Crescimento do INDE', 'INDE', cbIndicador, color='PEDRA'))
    