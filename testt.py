import streamlit as st

col1, col2, col3, col4 = st.columns([6, 1, 1, 1])

# Initialize the session state slider value if it doesn't exist
if "slider" not in st.session_state:
    st.session_state.slider = 0

def plus(value):
    if st.session_state.slider < 1000:
        st.session_state.slider += value

def minus(value):
    if st.session_state.slider > -1000:
        st.session_state.slider -= value

# Create the slider
with col1:
    slide_val = st.slider("Pick a number", -1000, 1000, key="slider")

with col2:
    add_one = st.button("+1", on_click=plus, args=(1,))
    remove_one = st.button("-1", on_click=minus, args=(1,))

with col3:
    add_five = st.button("+5", on_click=plus, args=(5,))
    remove_five = st.button("-5", on_click=minus, args=(5,))

with col4:
    add_ten = st.button("+10", on_click=plus, args=(10,))
    remove_ten = st.button("-10", on_click=minus, args=(10,))
