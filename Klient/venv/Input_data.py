import datetime


class InputData:
    list_of_available_statuses = ["In progress", "Closed", "New"]
    stars = "***************************************************"

    # Inputted by user
    title = None
    description = None
    person_from_list = None
    time_of_request = None
    status = None

    # def __init__(self):

    # Data inputted during create bug
    def inputting(self):
        try:
            print(self.stars)
            print("Creating new bug report")
            print("Input title: ")
            print("Input description: ")
            print(
                "\n\n1. Krzysztof Zerman\n2. Maciej Jakubowski\n\nInput number next to person you want to assign: ")
            self.time_of_request = datetime.datetime.now()
            print(self.time_of_request)
            print("Status: {}".format(str(self.list_of_available_statuses[2])))
            print(self.stars)
        except:
            print("\n{}\nError during create bug\n{}\n".format(self.stars, self.stars))
        return
