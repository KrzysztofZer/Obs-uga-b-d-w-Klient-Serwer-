# Main class
import Input_data
import sys
import save_created_data

user_level = None
user_login = "klient"
user_password = "serwer"


def menu():
    x = list_of_activities()
    if x == '1':
        create_bug()
        return
    elif x == '2':
        show_bugs()
        return
    elif x == '10':
        exit_menu()
        return
    else:
        number_out_of_range()
    return


def create_bug():
    object_to_create = Input_data.InputData()
    object_to_create.inputting()
    save_created_data.send_data(object_to_create)
    menu()


def number_out_of_range():
    print("****Pls provide number from list below!!!****")
    menu()


def show_bugs():
    print("Bug 1")
    print("Bug 2")
    menu()


def list_of_activities():
    print("1.  Create new bug report")
    print("2.  Show list of bugs")
    print("10. Exit")
    x = input("Input number of activity: ")
    print('\n\n')
    return x


def exit_menu():
    print("Program is ended")


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


# Login into app
login()
# Open menu
menu()

