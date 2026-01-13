import streamlit as st

st.set_page_config(page_title="Ganesh App", layout="centered")

st.title("🚀 My First Streamlit App")

st.write("If you can see this, deployment worked.")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}! Your app is running.")

