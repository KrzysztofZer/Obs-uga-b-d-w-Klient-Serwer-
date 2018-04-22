# To do

user_level = None
user_login = "klient"
user_password = "serwer"

def login():
    global user_login
    if input("Login: ") == user_login:
        if input("Password: ") == user_password:
            print("\n\n\n\n\nYou are successful logged in as {}\n".format(user_login))
        else:
            print("\nInvalid password!!!")
            login()
    else:
        print("\nInvalid login!!!")
        login()
    return