import streamlit as st
import pandas as pd
import numpy as np
import joblib
import utilidades
import globals

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
                st.subheader('**Aluno com baixa performance**')
            else:
                st.subheader('**Aluno com alta performance**')

        st.expander(':bulb: Considerações', expanded=False).write(""" Este modelo foi desenvolvido para avaliar o desempenho dos alunos, utilizando como base suas notas e um sistema de classificação chamado "pedras". Entre as categorias de pedras, destaca-se a "Quartzo", que representa alunos com baixo desempenho. Com isso, ao inserir as notas no modelo, ele pode prever se o aluno em questão tem risco de apresentar uma performance insatisfatória. Essa previsão permite que os responsáveis tomem medidas proativas, oferecendo o suporte necessário para melhorar o desempenho do aluno. """)

with tab2:
    st.write('**Relatório de performance**')
    st.write(""" Para determinar o modelo mais eficiente na previsão do desempenho escolar dos alunos, foi realizada uma análise comparativa envolvendo diversos algoritmos de aprendizado de máquina. Esses modelos foram treinados utilizando as informações fornecidas no dataset, abrangendo variáveis relacionadas ao desempenho escolar. Após o treinamento, os resultados de cada modelo foram avaliados e organizados em um dataframe estruturado. Esse dataframe contém informações detalhadas, incluindo o nome do modelo, os valores obtidos na validação cruzada, bem como as métricas de desempenho mais relevantes: F1 Score, Acurácia, Precision e Recall. Essas métricas foram escolhidas para garantir uma avaliação abrangente, especialmente considerando o equilíbrio entre precisão e sensibilidade nos casos de desbalanceamento de classes. """) 

    st.write(""" Com base na análise das métricas de desempenho, deu-se ênfase ao F1 Score como critério principal de avaliação devido ao desbalanceamento observado no dataset original. Essa escolha foi feita porque o F1 Score equilibra a precisão (precision) e a sensibilidade (recall), sendo ideal para cenários em que há classes desproporcionais. Após a comparação dos resultados entre os modelos testados, o Support Vector Machine (SVM) foi identificado como o mais adequado para resolver o problema proposto, apresentando o melhor desempenho em termos de F1 Score. """)

    st.dataframe(globals.df_model_report.style.highlight_max(axis=0, color='green'), use_container_width=True)    

    st.write("Os resultados obtidos com o modelo Support Vector Machine (SVM) são apresentados na tabela acima. O SVM obteve o melhor desempenho em termos de F1 Score, Acurácia, Precision e Recall, superando os demais modelos avaliados. Esses resultados reforçam a eficácia do SVM na previsão do desempenho escolar dos alunos, destacando sua capacidade de lidar com classes desbalanceadas e fornecer previsões precisas e confiáveis. Portanto, o SVM foi selecionado como o modelo final para a realização das previsões de desempenho dos alunos neste projeto.")   

    st.write("""Os testes e validações podem ser encontrados clicando [aqui](https://github.com/Rogeriom49/datathon_fiap/blob/main/notebooks/model_training.ipynb) """)          
