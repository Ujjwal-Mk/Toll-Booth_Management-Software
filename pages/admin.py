import streamlit as st
import time
import pathlib, sys
def disp():
    tab1, tab2 = st.tabs(['home','user info'])
    with tab1:
        st.subheader('Welcome to home page')
    with tab2:
        import backrooms
        backrooms.disp_info()