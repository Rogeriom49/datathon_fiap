import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval

st.header('**Dashboard**')


iframe_url = "https://app.powerbi.com/view?r=eyJrIjoiMGFmNDAzNTEtMWZkYS00NGFiLWEyN2YtMmRkZjIwNjUyZTA2IiwidCI6IjZkYzg3NGNlLWRkMmItNGFhOS05ZjBkLWFkYjkyNjlhNzU4MCJ9 "

components.iframe(iframe_url, width=1400, height=650)