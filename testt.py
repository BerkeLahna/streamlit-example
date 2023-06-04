import streamlit as st# slider value up to 10

col1, col2 = st.columns([3,1])

def plus_one():
    if st.session_state["slider"] < 10:
        st.session_state.slider += 1
    else:
        pass
    return


def minus_one():
    if st.session_state["slider"] < 10:
        st.session_state.slider -= 1
    else:
        pass
    return
# when creating the button, assign the name of your callback
# function to the on_click parameter
with col2:
    add_one = st.button("Add one to the slider", on_click=plus_one, key="add_one")
    remove_one = st.button("remove one from the slider", on_click=minus_one, key="minus_one")
# create the slider
with col1:
    slide_val = st.slider("Pick a number", 0, 10, key="slider")
