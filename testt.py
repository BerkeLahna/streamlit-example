import streamlit as st

st.title("Example")

def increment_value():
    st.session_state.numeric += st.session_state.val

def decrement_value():
    st.session_state.numeric -= st.session_state.val

def update_slider():
    st.session_state.slider = st.session_state.numeric

def update_numin():
    st.session_state.numeric = st.session_state.slider

col1, col2 = st.columns([3, 1])

with col1:
    slider_value = st.slider('Slider', min_value=0,
                             value=0,
                             max_value=5,
                             step=1,
                             key='slider', on_change=update_numin)

with col2:
    st.button("Increment", on_click=increment_value)
    st.number_input('Input', value=0, key='val', on_change=update_slider)
    st.button("Decrement", on_click=decrement_value)

st.write("Value:", st.session_state.numeric)
