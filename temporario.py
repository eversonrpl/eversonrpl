import streamlit as st
import pandas as pd
st.header("Cabeçalho")
st.toggle("Toggle")
st.text_area("enter text")
st.text_input("movie title", "life of briann")
st.selectbox(
  "Qual é a sua cor favorita?",
  ('azul', 'vermelho', 'verde'))
st.multiselect(
    "Qual é a sua cor favorita?",
    ["verde", "amarelo", "vermelho", "azul"],
)
agree = st.checkbox("Eu concordo")

if agree:
    st.write("ótimo!")
st.button("botão salvar")
