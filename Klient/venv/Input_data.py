import datetime


class InputData:
    list_of_available_statuses = ["In progress", "Closed", "New"]
    list_of_available_people = ["Krzysztof Zerman", "Maciej Jakubowski", "Unassigned"]
    stars = "***************************************************"

    # Inputted by user
    title = None
    description = None
    person_from_list = None
    time_of_request = None
    status = None

    def __init__(self, new_title, new_description, new_person_from_list, new_time_of_request, new_status):
        self.title = new_title
        self.description = new_description
        self.person_from_list = new_person_from_list
        self.time_of_request = new_time_of_request
        self.status = new_status
        return 

    # Data inputted during create bug
    def inputting(self):
        try:
            print(self.stars)
            print("Creating new bug report")

            # Inputting title
            self.title = input("Input title: ")

            # Inputting description
            self.description = input("Input description: ")

            # Inputting person to assign
            self.display_list(self.list_of_available_people)
            number_of_person = input("Input number next to person you want to assign: ")
            while True:
                if number_of_person.isdigit() and 0 <= int(number_of_person) < len(self.list_of_available_people):
                    break
                number_of_person = input("Input number next to person you want to assign: ")
            self.person_from_list = self.list_of_available_people[int(number_of_person)]

            # Setting time of request
            self.time_of_request = datetime.datetime.now()

            # Setting status
            self.status = self.list_of_available_statuses[2]
            print(self.stars)

            # Everything OK?
            self.show_bug()
        except:
            print("\n{}\nError during create bug\n{}\n".format(self.stars, self.stars))
        return

    # Show user bug data
    def show_bug(self):
        print("\n\n\n{}".format(self.stars))
        print("Title: {0}\nDescription: {1}\nAssigned person: {2}\nTime: {3}\nStatus: {4}".format(self.title, self.description, self.person_from_list, self.time_of_request, self.status))
        while True:
            a = input("\nAll data is correct? (y/n): ")
            if a is 'n':
                self.inputting()
            if a is 'y':
                break
        return
    
    # Method displaying list
    def display_list(self, list):
        i = 0
        for x in list:
            print("{}. {}".format(i, x))
            i = i + 1
        return 
    

