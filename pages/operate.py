import streamlit as st
import time,pathlib,sys
def disp():
    def submit():
        st.session_state.submitted=True
    def reset():
        st.session_state.submitted=False
    with st.container():
        module_dir = pathlib.Path(__file__).parent.parent
        sys.path.append(str(module_dir))
        from backend import database as db
        dest = db.get_dest()
        vehicle = db.get_vehicle_type()
        fare = 0
        with st.form("my_form2"):
            st.text_input("Vehicle Registration Number: ",key='reg_no')
            st.selectbox("Vehicle Type",options=vehicle,key='type',index=None)
            st.selectbox("Destination",options=dest,key='dest', index=None)
            st.form_submit_button("Submit",on_click=submit)
        if 'submitted' in st.session_state and st.session_state.submitted==True:
            conn, cursor = db.init_conn()
            fare = db.get_fare(st.session_state.dest, st.session_state.type)
            # print(st.session_state)
            cursor.execute(f"INSERT INTO ticket_generate(ticket_id,emp_username, place, vehicle_type, vehicle_registration_number, cost) VALUES \
                (UUID(),'{st.session_state.name}', '{st.session_state.dest}', '{st.session_state.type}', '{st.session_state.reg_no}', {fare[0]})")
            conn.commit()
            st.success("Ticket Generated successfully")
            time.sleep(2)
            reset()