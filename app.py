#!/usr/bin/env python3

import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app!")
st.write("You can now start building your app by adding more Streamlit components.")
st.write("For example, you can add a button like this:")
if st.button("Click me"):
    st.write("Button clicked!")
