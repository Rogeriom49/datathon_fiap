import streamlit as st

st.title('**Introdução**')

tab1, tab2, tab3 = st.tabs(['Sobre a Passos Mágicos', 'Sobre o Projeto', 'Dicionário'])

with tab1:
    st.write('teste')

with tab2:
    st.write('teste2')

with tab3:
    st.write('teste3')