import streamlit as st
from streamlit_modal import Modal
import time,pathlib,sys
modal = Modal(key="Demo Key",title="test")
def disp():
    def popup():
        success = st.success("Ticket Generated Successfully")
        time.sleep(1)
        success.empty()
    with st.container():
        module_dir = pathlib.Path(__file__).parent.parent
        sys.path.append(str(module_dir))
        from backend import database as db
        
        with st.form("my_form2"):
            st.text_input("Vehicle Registration Number: ",key='reg_no')
            st.selectbox("Vehicle Type",options=['car','bus','truck'],key='type',index=None)
            st.text_input("Destination",key='dest')
            st.form_submit_button("Submit",on_click=popup)
        
        