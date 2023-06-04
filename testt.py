import streamlit as st

st.title("Example")

col1, col2 = st.columns([3, 1])

with col1:
    age = st.slider("Enter age:", min_value=18, max_value=100, value=30, key="age_slider")

with col2:
    age_input = st.number_input(" ", min_value=18, max_value=100, value=30, key="age_input")

if age != age_input:
    st.session_state.age_slider = age_input
    st.session_state.age_input = age

st.write(f"Age: {age}")
