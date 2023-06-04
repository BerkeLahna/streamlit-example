import streamlit as st

st.title("Example")

def update_slider():
    st.session_state.slider = st.session_state.numeric

def update_numin():
    st.session_state.numeric = st.session_state.slider

val = st.number_input('Input', value=0, key='numeric', on_change=update_slider)

slider_value = st.slider('slider', min_value=0,
                         value=val,
                         max_value=5,
                         step=1,
                         key='slider', on_change=update_numin)
