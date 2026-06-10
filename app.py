import streamlit as st

st.title("Тестовое приложение")
st.write("Если вы видите этот текст — всё работает!")

name = st.text_input("Как вас зовут?")

if name:
    st.write(f"Привет, {name}!")
