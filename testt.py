import streamlit as st# slider value up to 10

col1, col2 = st.columns([3,1])
container = st.container()
def plus_one():
    if st.session_state["slider"] < 1000:
        st.session_state.slider += 1
    else:
        pass
    return


def minus_one():
    if st.session_state["slider"] > -1000:
        st.session_state.slider -= 1
    else:
        pass
    return
# when creating the button, assign the name of your callback
# function to the on_click parameter
with col2:
    with container:
        add_one = st.button("+1", on_click=plus_one, key="add_one")
        remove_one = st.button("-1", on_click=minus_one, key="minus_one")
# create the slider
with col1:
    slide_val = st.slider("Pick a number", -1000, 1000, key="slider")
