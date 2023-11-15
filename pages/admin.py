import streamlit as st
import time
import pathlib, sys
import pandas as pd
def disp():
    tab1, tab2 = st.tabs(['home','user info'])
    with tab1:
        st.subheader('Welcome to home page')
        module_dir = pathlib.Path(__file__).parent.parent
        sys.path.append(str(module_dir))
        from backend import database as db
        conn,cursor = db.init_conn()
        operate_str = "SELECT * FROM ticket_generate;"
        st.dataframe(db.get_df(operate_str),use_container_width=True)
    with tab2:
        import backrooms
        backrooms.disp_info()