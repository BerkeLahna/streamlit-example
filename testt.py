import streamlit as st

# Define CSS style for smaller button font
button_style = """
    <style>
    .smaller-font {
        font-size: 12px;
    }
    </style>
"""

# Display the CSS style
st.markdown(button_style, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([6, 0.5, 0.5, 0.5])

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
    # Add the 'smaller-font' CSS class using Markdown syntax
    add_one = st.button("+1", on_click=plus, args=(1,), key="add_one", help="add_one")
    st.markdown('<p class="smaller-font">' + st.help(add_one) + '</p>', unsafe_allow_html=True)

    remove_one = st.button("-1", on_click=minus, args=(1,), key="remove_one", help="remove_one")
    st.markdown('<p class="smaller-font">' + st.help(remove_one) + '</p>', unsafe_allow_html=True)

with col3:
    add_five = st.button("+5", on_click=plus, args=(5,), key="add_five", help="add_five")
    st.markdown('<p class="smaller-font">' + st.help(add_five) + '</p>', unsafe_allow_html=True)

    remove_five = st.button("-5", on_click=minus, args=(5,), key="remove_five", help="remove_five")
    st.markdown('<p class="smaller-font">' + st.help(remove_five) + '</p>', unsafe_allow_html=True)

with col4:
    add_ten = st.button("+10", on_click=plus, args=(10,), key="add_ten", help="add_ten")
    st.markdown('<p class="smaller-font">' + st.help(add_ten) + '</p>', unsafe_allow_html=True)

    remove_ten = st.button("-10", on_click=minus, args=(10,), key="remove_ten", help="remove_ten")
    st.markdown('<p class="smaller-font">' + st.help(remove_ten) + '</p>', unsafe_allow_html=True)
