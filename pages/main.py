import streamlit as st
import pathlib, sys

def homepage(boolean,username,authenticator):
    if not boolean:
        return
    if db.get_level(username)=='admin':
        st.header('Welcome to admin homepage')
        import admin as ad
        ad.disp()
        authenticator.logout("Logout","main")
    if db.get_level(username)=='operator':
        st.header(f'Welcome to toll operator homepage')
        import operate as op
        op.disp()
        authenticator.logout("Logout","main")

if __name__ == '__main__':
    module_dir = pathlib.Path(__file__).parent.parent
    sys.path.append(str(module_dir))
    import auth as au
    # st.title('Hello')
    from backend import database as db
    db.init_conn()
    # dbobj = db.DatabaseHandler()
    # st.button('Test Frontend',on_click=au.test)
    boolean, username, authenticator = au.user_login()
    homepage(boolean,username,authenticator)