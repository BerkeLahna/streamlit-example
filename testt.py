import streamlit as st# slider value up to 10

col1, col2 = st.columns(2)

def plus_one():
    if st.session_state["slider"] < 10:
        st.session_state.slider += 1
    else:
        pass
    return

# when creating the button, assign the name of your callback
# function to the on_click parameter
add_one = col2.st.button("Add one to the slider", on_click=plus_one, key="add_one")

# create the slider
slide_val = col1.st.slider("Pick a number", 0, 10, key="slider")
