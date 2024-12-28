import streamlit as st
import pandas as pd
import numpy as np
import joblib
import utilidades

st.header('**Modelo de Machine Learning**')

st.markdown(""" Preencha os campos abaixo para realizar a previsão""")

modelo = joblib.load('best_model_support_vector_machine.pkl')

tab1, tab2 = st.tabs(['Previsões', 'Relatório'])

with tab1:
    with st.form(key='form', enter_to_submit=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            iaa = st.number_input('IAA', min_value=0, max_value=10, value=5)
            ipp = st.number_input('IPP', min_value=0, max_value=10, value=5)

        with col2:
            ieg = st.number_input('IEG', min_value=0, max_value=10, value=5)
            ipv = st.number_input('IPV', min_value=0, max_value=10, value=5)

        with col3:
            ips = st.number_input('IPS', min_value=0, max_value=10, value=5)                
            ian = st.number_input('IAN', min_value=0, max_value=10, value=5)                

        with col4:
            ida = st.number_input('IDA', min_value=0, max_value=10, value=5)

        co5,col6,col7 = st.columns([1,1,1], border=False, vertical_alignment='center')

        with col6:
            submit = st.form_submit_button('Realizar previsão', type='primary', use_container_width=True, help='Clique para realizar a previsão de performance do aluno')
        
        if submit:
            dados = {'IAA':iaa, 'IEG':ieg, 'IPS':ips, 'IDA':ida, 'IPP':ipp, 'IPV':ipv, 'IAN':ian}
            data = pd.DataFrame([dados])
            resultado = utilidades.forecast_performance(data, modelo)
            if resultado == 0:
                st.write('**Aluno com baixa performance**')
            else:
                st.write('**Aluno com alta performance**')
