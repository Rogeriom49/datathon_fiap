import streamlit as st
import globals
import os

st.set_page_config(layout='wide', 
                   page_title='Datathon - FIAP')

col1, col2,col3, col4 = st.columns(4, gap='small', vertical_alignment='center', border=False)

with col2:
    st.image('assets/images/fiap.png', width=160, clamp=True)

with col3:
    st.image('assets/images/passos.png', width=200, clamp=True)

pages = [
        st.Page(page="paginas/introducao.py", title="Introdução", default=True),
        st.Page(page="paginas/analysis.py", title="Análise", default=False),
        st.Page(page="paginas/model.py", title="Modelo", default=False),
        st.Page(page="paginas/technologies.py", title="Técnologias", default=False),
        st.Page(page="paginas/conclusao.py", title="Conclusão", default=False),  
]

with st.sidebar:
    st.subheader('Integrantes',divider='gray')
    st.markdown(""" RM353394 - Gabriel da Silva Sousa """)
    st.markdown(""" RM353861 - Rogério Paulo Marcon Júnior """)
    st.markdown(""" RM354166 - Thaís Rpdrigues Gasparetto """)
    st.markdown(""" RM353227 - Vinicius dos Santos Aquino""")

    st.divider()

    st.subheader("Instalando as dependências do app localmente")
    st.code(body="python -m venv venv", language="shell")
    st.code(body="source venv/Scripts/activate", language="shell")
    st.code(body="pip install -r requirements.txt", language="shell")

    st.divider()

    st.subheader("Executando localmente")
    st.code(body="streamlit run index.py", language="shell")

    st.divider()

    st.subheader("Repositórios do projeto")
    st.markdown(f""" <div>
                        <a href="{globals.pd}" target="_blank"><img src="assets/images/github.png" width="30"/></a>     
                     </div> """, unsafe_allow_html=True)

pg = st.navigation(pages)

pg.run()

