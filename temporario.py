import streamlit as st
st.header("Cabeçalho")
st.toggle("Toggle")
st.text_area("enter text")
st.text_input("movie title", "life of briann")
st.selectbox(
  "Qual é a sua cor favorita?",
  ('azul', 'vermelho', 'verde'))
st.button("botão salvar")
