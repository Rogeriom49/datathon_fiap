import streamlit as st
import os

st.set_page_config(layout='wide', 
                   page_title='Datathon')

pages = [
        st.Page(page="paginas/introducao.py", title="Introdução", default=True),
        st.Page(page="paginas/analysis.py", title="Análise", default=False),
        st.Page(page="paginas/model.py", title="Modelo", default=False),
        st.Page(page="paginas/technologies.py", title="Técnologias", default=False),
        st.Page(page="paginas/conclusao.py", title="Conclusão", default=False),  
]

pg = st.navigation(pages)

pg.run()

