import streamlit as st

st.title("Example")

if "age" not in st.session_state:
    st.session_state.age = 30

col1, col2 = st.columns([3, 1])

with col1:
    age = st.slider("Enter age:", min_value=18, max_value=100, value=st.session_state.age)

with col2:
    age_input = st.number_input(" ", min_value=18, max_value=100, value=st.session_state.age)

st.session_state.age = age_input

st.write(f"Age: {age}")
