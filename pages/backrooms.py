import streamlit as st
import pathlib,sys

def disp_info():
        st.header("List of users:")
        module_dir = pathlib.Path(__file__).parent.parent
        sys.path.append(str(module_dir))
        from backend import database as db
        with st.container():
            st.dataframe(db.get_df('''SELECT username as 'Username', CONCAT(f_name, ' ', l_name) AS Name, address as Address, date_of_joining as 'Date of Joining',
                                        CASE
                                            WHEN auth_level = '0' THEN 'Admin'
                                            WHEN auth_level = '1' THEN 'Toll Operator'
                                            ELSE 'Unknown Role'
                                        END AS Role
                                    FROM usr_info1;'''),use_container_width=True)
        with st.container():
            def submitted():
                st.session_state.submitted = True
            def reset():
                st.session_state.submitted = False
            with st.expander('Create New User'):
                with st.form("User Form",clear_on_submit=True):
                    st.text_input("Username",key="uname")
                    st.text_input("Password",type='password',key='Pass')
                    st.text_input("First Name",key='f_name')
                    st.text_input("Middle Initials",key='minit')
                    st.text_input("Last Name",key='l_name')
                    st.text_input("Address",key='address')
                    st.selectbox("Authorization Level",['0','1'],index=1,key='auth_lvl')
                    st.form_submit_button("Submit",on_click=submitted)
            if 'submitted' in st.session_state and st.session_state.submitted == True:
                uname = st.session_state.uname
                Pass = st.session_state.Pass
                f_name = st.session_state.f_name
                minit = st.session_state.minit
                l_name = st.session_state.l_name
                addr = st.session_state.address
                auth_lvl = st.session_state.auth_lvl
                db.add_usr(uname,Pass,f_name,minit,l_name,auth_lvl,addr)
                reset()
                st.success("New User added")
        with st.container():
            def delete_submission():
                st.session_state.deleted = True
            def delete_reset():
                st.session_state.deleted = False
                
            with st.container():
                user_dict = db.get_usr_names() 
                with st.expander("Delete User"):
                    with st.form('Delete User'):
                        st.selectbox('Name of User',options=list(user_dict.keys()),index=None,key='usr_name')
                        st.form_submit_button("Delete", on_click=delete_submission)
                if 'deleted' in st.session_state and st.session_state.deleted == True:
                    # print(type(user_dict[st.session_state.usr_name]))
                    db.delete_user(user_dict[st.session_state.usr_name])
                    st.success(f"Successfully Deleted {st.session_state.usr_name}")
                    delete_reset()
