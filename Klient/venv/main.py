# Main class
import datetime

list_of_available_statuses = ["In progress", "Closed", "New"]
stars = "***************************************************"

# Inputted by user
title = None
description = None
person_from_list = None
time_of_request = None
status = None

# Data inputted during create bug
def input_data():
    # Global values
    global title
    global description
    global person_from_list
    global time_of_request
    global status
    global list_of_available_statuses

    try:
        print(stars)
        print("Creating new bug report")
        print("Input title: ")
        print("Input description: ")
        print("\n\n1. Krzysztof Zerman\n2. Maciej Jakubowski\n\nInput number next to person you want to assign: ")
        time_of_request = datetime.datetime.now()
        print(time_of_request)
        print("Status: {}".format(str(list_of_available_statuses[2])))
        print(stars)
    except:
        print ("\n{}\nError during create bug\n{}\n".format(stars, stars))
    return


input_data()
