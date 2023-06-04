import streamlit as st

st.title("Example")

col1, col2 = st.columns([3, 1])

with col1:
    age = st.slider("Enter age:", min_value=18, max_value=100, value=30)

with col2:
    age_input = st.number_input( min_value=18, max_value=100, value=30)

st.write(f"Age: {age}")
