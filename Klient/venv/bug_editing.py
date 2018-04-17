edited_object = None

def menu_of_editing(object_to_edit):
    global edited_object
    edited_object = object_to_edit
    print("\n************Menu of editing**************")
    list_of_edit_possibilities()
    x = input("Pls input option by write number")
    if x == '1':
        change_status()
        return
    elif x == '2':
        change_title()
        return
    elif x == '3':
        change_description()
        return
    elif x == '4':
        change_assign_person()
        return
        change_description()
    elif x == '5':
        return
    else:
        number_out_of_range()


# To do
def change_status():
    print("Changing status")
    return


# To do
def change_title():
    print("Changing title")
    return


# To do
def change_description():
    print("Changing description")
    return


# To do
def change_assign_person():
    print("Changing assign person")
    return


# To do
def change_assign_person():
    print("Changing assign person")
    return


def list_of_edit_possibilities():
    print("1. Status")
    print("2. Title")
    print("3. Description")
    print("4. Assigned person")
    print("5. Cancel")


def number_out_of_range():
    print("****Pls provide number from list below!!!****")
    menu()
