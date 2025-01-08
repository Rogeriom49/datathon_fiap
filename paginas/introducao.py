import streamlit as st

st.title('**Introdução**')

tab1, tab2, tab3 = st.tabs(['Sobre a Passos Mágicos', 'Sobre o Projeto', 'Dicionário'])

with tab1:
    st.write('teste')

with tab2:
    st.write('teste2')

with tab3:
    col1, col2, col3= st.columns(3)

    with col1:
        st.subheader('**IAN**')
        st.write('Indicador de adequação de nível')
        st.write('Originário de resgistro administrativos')
    with col2:
        st.subheader('**IDA**')
        st.write('Indicador de desempenho acadêmico')
        st.write('Notas de provas e média geral universitária')
    with col3:
        st.subheader('**IEG**')
        st.write('Indicador de engajamento')                
        st.write('Registro de entregas de lições de casa e voluntariado')                
     
    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader('**IAA**')
        st.write('Indicador de autoavaliação')           
        st.write('Questionário de autoavaliação individual')           

    with col5:
        st.subheader('**IPP**')
        st.write('Indicador psicopedagógico')
        st.write('Questionário de avalidação dos pedagogos e professores')
    with col6:
        st.subheader('**IPV**')
        st.write('Indicador do ponto da virada')            
        st.write('Questionário de avalidação dos pedagogos e professores')