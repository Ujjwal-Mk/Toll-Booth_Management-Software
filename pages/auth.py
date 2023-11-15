import streamlit as st
import streamlit_authenticator as stauth
import time, pathlib, sys

def user_login():

    module_dir = pathlib.Path(__file__).parent.parent
    sys.path.append(str(module_dir))

    usernames = []
    names = []
    hashed_passwords = []    
    from backend import database as db
    try:
        user_data = db.get_login_user_info()
        if user_data is not None:
            names, usernames, hashed_passwords = user_data
    except Exception as e:
        st.error("Server down")
        return (0, None,None)

    
    credentials = {"usernames": {}}

    for uname, name, pwd in zip(usernames, names, hashed_passwords):
        user_dict = {"name": name, "password": pwd}
        credentials["usernames"].update({uname: user_dict})
    #print(credentials)

    authenticator = stauth.Authenticate(credentials, "cookkkie", "random_key", cookie_expiry_days=1)

    st.title("SE Project")

    name, authentications_status, username = authenticator.login("Login", "main")


    if authentications_status is False:
        error = st.error("Username/password is incorrect")
        time.sleep(2)
        error.empty()
        return (0,username,authenticator)

    if authentications_status is None:
        warn = st.warning("Please enter Username and password")
        time.sleep(2)
        warn.empty()
        return (0,username,authenticator)
    
    if authentications_status:

        # authenticator.logout("Logout", "main")
        return (1,username,authenticator)
    
