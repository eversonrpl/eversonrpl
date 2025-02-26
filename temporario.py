import streamlit as st
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
st.button("botão salvar")
