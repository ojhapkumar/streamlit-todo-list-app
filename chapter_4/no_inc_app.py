import streamlit as st
 
st.info(st.session_state)
if "number" not in st.session_state:
    st.session_state.number = 0
 
if st.button("Increment"):
    st.session_state.number += 1
 
st.info(f"Number: {st.session_state.number}")
 