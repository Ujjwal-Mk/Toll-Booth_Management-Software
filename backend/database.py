import mysql.connector
import pandas as pd
import streamlit_authenticator as stauth

connection = None
cursor = None

def init_conn():
    global connection, cursor
    try:
        if connection == None:
            db_config = {
                'host':'localhost',
                "user": "seproj",
                "password": "seproj",
                "database": "toll_booth"
            }
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
        return connection,cursor
    except Exception as e:
        print(e)

def get_login_user_info():
    _, cursor = init_conn()
    try:
        usernames = []
        passwords = []
        names = []

        # Query to fetch usernames and passwords
        cursor.execute('SELECT username, CONCAT(f_name, " ", l_name) as name, hashed_pass FROM login_user_info;')
        # Fetching all the rows as a list of tuples
        user_data = cursor.fetchall()

        # Extract usernames and passwords from the fetched data
        for username, name, password in user_data:
            usernames.append(username)
            passwords.append(password)
            names.append(name)

        return (names,usernames, passwords)
    except Exception as e:
        print(e)


def get_df(operate_str):
    _,cursor = init_conn()
    cursor.execute(operate_str)
    if cursor.description!=None:
        cols=[i[0] for i in cursor.description]
        rows=cursor.fetchall()
    return (pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]))


def add_usr(uname,Pass,f_name,minit,l_name,auth_lvl,address):
    connection, cursor = init_conn()
    try:
        dummy_list = []
        dummy_list.append(Pass)
        hash_pass = stauth.Hasher(dummy_list).generate()[0]

        operate_str = 'INSERT INTO user_info (f_name,minit,l_name,username,hashed_pass,auth_level) VALUES (%s,%s,%s,%s,%s,%s)'
        data = (f_name,minit,l_name,uname,hash_pass,auth_lvl)

        cursor.execute(operate_str,data)

        operate_str1 = 'INSERT INTO usr_info1 (f_name,minit,l_name,username,hashed_pass,auth_level,address,date_of_joining) VALUES (%s,%s,%s,%s,%s,%s,%s,CURDATE())'
        data = (f_name,minit,l_name,uname,Pass,auth_lvl,address)
        cursor.execute(operate_str1,data)
        print("\nnew user added\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
         if connection:
              connection.commit()


def get_level(username):
    try:
        connection,cursor = init_conn()
        auth_levels = []
        operate_str1 = (f"SELECT auth_level FROM login_user_info WHERE username='{username}'")
        cursor.execute(operate_str1)
        user_data = cursor.fetchone()
        return user_data[0]
    
    except mysql.connector.Error as err:
        print(f"Error{err}")

def get_usr_names():
    try:
        _, cursor = init_conn()
        names = []
        usrids = []
        cursor.execute('SELECT usrid, CONCAT(f_name, " ", l_name) as names FROM usr_info1;')
        rows = cursor.fetchall()
        for usrid,name in rows:
            usrids.append(usrid)
            names.append(name)
        usr_dict = dict(zip(names,usrids))
        # names_list = list(usr_dict.keys())
        # for namers in names_list:
        #     print(usr_dict[namers])
        return (usr_dict)
    except Exception as e:
        print(f"get_usr_names error:{e}")

def delete_user(usrid: int) -> None:
    try:
        connection,cursor = init_conn()
        operate_str = f"DELETE FROM usr_info1 WHERE usrid = {usrid}"
        # print(operate_str)
        cursor.execute(operate_str)
        operate_str1 = f"DELETE FROM usr_info WHERE usrid = {usrid}"
        # print(operate_str1)
        cursor.execute(operate_str1)
        connection.commit()
    except Exception as e:
        print(f"delete user error:{e}")

def get_dest():
    try:
        conn,cursor = init_conn()
        operate_str = "SELECT destination from cost_matrix;"
        cursor.execute(operate_str)
        dests = cursor.fetchall()
        # print(dests)
        dest_final=[]
        for place in dests:
            dest_final.append(place[0])
        return dest_final
    except Exception as e:
        print(f'get_dest error:\n{e}')

def get_vehicle_type():
    try:
        conn,cursor = init_conn()
        operate_str = 'SELECT Car,Bus,Truck from cost_matrix;'
        cursor.execute(operate_str)
        _ = cursor.fetchall()
        vehicle_type = [i[0] for i in cursor.description]
        return vehicle_type
    except Exception as e:
        print(f'get_vehicle_type error:\n{e}')

def get_fare(dest, vehicle):
    try:
        conn,cursor = init_conn()
        operate_str = f"SELECT {vehicle} from cost_matrix where destination='{dest}'"
        cursor.execute(operate_str)
        price = cursor.fetchall()
        return price[0]
    except Exception as e:
            print(f'get_fare error:\n{e}')