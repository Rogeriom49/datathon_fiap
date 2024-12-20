import streamlit as st

st.title('**Introdução**')

tab1, tab2 = st.tabs(['Sobre a Passos Mágicos', 'Sobre o Projeto'])

with tab1:
    st.write('teste')

with tab2:
    st.write('teste2')