import streamlit as st
import pathlib,sys

def disp_emp_info():
        st.header("List of users:")
        module_dir = pathlib.Path(__file__).parent.parent
        sys.path.append(str(module_dir))
        from backend import database as db
        with st.container():
            st.dataframe(db.get_df('''SELECT usrid as 'User ID', CONCAT(f_name, ' ', l_name) AS Name, address as Address, date_of_joining as 'Date of Joining',
                                        CASE
                                            WHEN auth_level = 'admin' THEN 'Admin'
                                            WHEN auth_level = 'operator' THEN 'Toll Operator'
                                            ELSE 'Unknown Role'
                                        END AS Role
                                    FROM employee_info;'''),use_container_width=True)
        with st.container():
            def submitted():
                st.session_state.submitted = True
            def reset():
                st.session_state.submitted = False
            with st.expander('Create New Employee'):
                with st.form("Employee Form",clear_on_submit=True):
                    st.text_input("First Name",key='f_name')
                    st.text_input("Middle Initials",key='minit')
                    st.text_input("Last Name",key='l_name')
                    st.text_input("Address",key='address')
                    st.selectbox("Authorization Level",['admin','operator'],index=1,key='auth_lvl')
                    st.form_submit_button("Submit",on_click=submitted)
            if 'submitted' in st.session_state and st.session_state.submitted == True:
                f_name = st.session_state.f_name
                minit = st.session_state.minit
                l_name = st.session_state.l_name
                addr = st.session_state.address
                auth_lvl = st.session_state.auth_lvl
                db.add_employee(f_name,minit,l_name,auth_lvl,addr)
                reset()
                st.success("New User added")

        #Deletion
        with st.container():
            def delete_submission():
                st.session_state.deleted = True
            def delete_reset():
                st.session_state.deleted = False
                
            with st.container():
                #user_dict = db.get_usr_names() 
                with st.expander("Delete Employee"):
                    with st.form('Delete Employee'):
                        #st.selectbox('ID of Employee',options=list(user_dict.keys()),index=None,key='uid')
                        uid = ""
                        st.text_input("ID of Employee", key=uid)
                        st.form_submit_button("Delete", on_click=delete_submission)
                if 'deleted' in st.session_state and st.session_state.deleted == True:
                    # print(type(user_dict[st.session_state.usr_name]))
                    db.delete_employee(uid)
                    st.success(f"Successfully Deleted {st.session_state.uid}")
                    delete_reset()
