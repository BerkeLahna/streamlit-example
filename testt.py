import streamlit as st# slider value up to 10

col1, col2,col3,col4 = st.columns([6,0.5,0.5,0.5])

def plus(value):
    if st.session_state["slider"] < 1000:
        st.session_state.slider += value
    else:
        pass
    return


def minus(value):
    if st.session_state["slider"] > -1000:
        st.session_state.slider -= value
    else:
        pass
    return
# when creating the button, assign the name of your callback
# function to the on_click parameter

# create the slider
with col1:
    slide_val = st.slider("Pick a number", -1000, 1000, key="slider")
with col2:
    add_one = st.button("+1", on_click=plus(1))
    remove_one = st.button("-1", on_click=minus(1))
with col3:
    add_one = st.button("+5", on_click=plus(5))
    remove_one = st.button("-1", on_click=minus(5))
    
with col4:
    add_one = st.button("+10", on_click=plus(10))
    remove_one = st.button("-1", on_click=minus(10))
