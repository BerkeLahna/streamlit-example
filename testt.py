import streamlit as st

st.title("Example")

def update_slider():
    st.session_state.slider = st.session_state.numeric

def update_numin():
    st.session_state.numeric = st.session_state.slider

col1, col2 = st.columns([3, 1])

with col1:
    slider_value = st.slider('slider', min_value=0,
                             value=0,
                             max_value=5,
                             step=1,
                             key='slider', on_change=update_numin)

with col2:
    if st.button("Increment"):
        st.session_state.slider += st.number_input.value

    st.number_input('Input', value=0, key='numeric', on_change=update_slider)

    if st.button("Decrement"):
        st.session_state.slider -= st.number_input.value
