# Main class
import Input_data
import sys


def menu():
    x = str(list_of_activities())
    print("x == {}".format(x))
    return {
        "1": create_bug(),
        "2": show_bugs(),
        "10": print("Program is ended")
    }.get(x, number_out_of_range())


def create_bug():
    object_to_create = Input_data.InputData()
    object_to_create.inputting()
    menu()


def number_out_of_range():
    print("Pls provide number from list below!!!\n")
    menu()


def show_bugs():
    print("Bug 1")
    print("Bug 2")
    menu()


def list_of_activities():
    print("\n\n1.  Create new bug report")
    print("2.  Show list of bugs")
    print("10. Exit")
    x = input("Input number of activity: ")
    return x


# Open menu
menu()

