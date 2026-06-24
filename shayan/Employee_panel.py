class Line():
    def __init__(self, name: str, origin: str, destination: str, count: int, stations: list):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.count = count
        self.stations = stations

    def __str__(self):
        return f"{BLUE}line name: {self.name}{RESET} -- origin: {self.origin} -- destination:" \
               f" {self.destination} -- number of stations: {self.count} -- stations: {self.stations}"


lines = {}


class Employee():
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Train():
    def __init__(self, name, move_line, speed: int, waiting_time: int, stars, ticket_price: int, capacity: int):
        self.name = name
        self.moveline = move_line
        self.speed = speed
        self.waiting_time = waiting_time
        self.stars = stars
        self.ticket_price = ticket_price
        self.capacity = capacity


BLUE = '\033[94m'
RESET = '\033[0m'
RED = '\033[91m'


def emp_panel():
    print("1: Add new line\n2: Update line\n3: Remove line\n4: Show lines info\n"
          "5: Add Train\n6: Update Train info\n7: Remove Train\n8: Show Trains info\n"
          "9: Exit to main menu")
    choice = input(f"Please select an option ({BLUE}1-9{RESET}): ")
    if choice == "1":
        return add_line()
    elif choice == "2":
        return update_line()
    elif choice == "3":
        return remove_line()
    elif choice == "4":
        return show_lines()
    elif choice == "5":
        return add_train()
    elif choice == "6":
        return update_train()
    elif choice == "7":
        return remove_train()
    elif choice == "8":
        return show_trains()
    elif choice == "9":
        return main_menu()
    else:
        print(f"{RED}Please select 1-9 !!!\n{RESET}")
        return emp_panel()


def letter_please(prompt):
    while True:
        value = input(prompt).strip()
        if value.isalpha() == True:
            return value
        else:
            print(f"{RED}use a-z A-Z as a correct input !{RESET}\n")


def number_please(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() == True:
            return int(value)
        else:
            print(f"{RED}use numbers only !!! {RESET}\n")


def add_line():
    stations = []
    print("\n--- Adding new line ---\n")
    while True:
        name = letter_please("Enter line name : ")
        if name in lines.keys():
            print(f"{RED} this line is already exist !!!\n {RESET}")
        else:
            break
    origin = letter_please("Origin city : ")
    destination = letter_please("Destination city : ")
    count = number_please("Enter the number of Stations : ")
    print(f"you have {count} stations ")
    i = 1
    while i <= count:
        station = letter_please(f"Enter station {i} name : ")
        if station not in stations:
            stations.append(station)
            i += 1
        else:
            print(f"{RED}this station is already exist !{RESET}")

    new_line = Line(name, origin, destination, count, stations)
    lines[name] = new_line
    print("new line successfully added : \n", new_line, "\n")
    return emp_panel()


def update_line():
    choise = input("select _1_ for update or select _2_ for exit : ")
    if choise == "1" and len(lines.keys()) != 0:
        while True:
            line_name = input("Enter line name please : ")
            if line_name in lines.keys():
                print(lines[line_name])
                while True:
                    choise = input(
                        "please select an option\n 1:name\n 2:origin\n 3:destination\n 4:stations\n 5:exit : ")
                    if choise == "1":
                        while True:
                            new_name = letter_please("Enter line name : ")
                            if new_name in lines.keys():
                                print(f"{RED} this line is already exist !!!\n {RESET}")
                            else:
                                print(f"Name updated successfully: {line_name} to {new_name}")
                                lines[line_name].name = new_name
                                break
                    elif choise == "2":
                        new_origin = letter_please("Origin city : ")
                        print(f"Origin updated successfully: {lines[line_name].origin} to {new_origin}")
                        lines[line_name].origin = new_origin

                    elif choise == "3":
                        new_destination = letter_please("Destination city : ")
                        print(f"Destination updated successfully: {lines[line_name].destination} to {new_destination}")
                        lines[line_name].destination = new_destination
                    elif choise == "4":
                        new_count = number_please("Enter the number of Stations : ")
                        new_stations = []
                        print(f"you have {new_count} stations ")
                        i = 1
                        while i <= new_count:
                            station = letter_please(f"Enter station {i} name : ")
                            if station not in new_stations:
                                new_stations.append(station)
                                i += 1
                            else:
                                print(f"{RED}this station is already exist !{RESET}")
                        print(f"Stations updated successfully : {lines[line_name].stations} to {new_stations}")
                        lines[line_name].count = new_count
                        lines[line_name].stations = new_stations

                    elif choise == "5":
                        return update_line()
                    else:
                        print(f"{RED}select a number correctly !!{RESET}")
            else:
                print(f"{RED}there no line with name {line_name}{RESET}\n")
                return update_line()

    elif choise == "1" and len(lines.keys()) == 0:
        print(f"{RED}there is no line yet - go make a line first !!{RESET}")
        return emp_panel()
    elif choise == "2":
        return emp_panel()
    else:
        print(f"{RED}select carefully !!{RESET}")
        return update_line()


def remove_line():
    while True:
        choice = input("enter 1 for removing lines or enter 2 and back to main menu : ")
        if choice == "1":
            if len(lines.keys()) != 0:
                print("\n---Removing Line---\n")
                line_name = letter_please("Enter line name : ")
                if line_name in lines.keys():
                    while True:
                        confirm = input(f"Are you sure to remove line??\n {lines[line_name]} (yes/no) : ").lower()
                        if confirm == "yes":
                            lines.pop(line_name)
                            print(f"{line_name} removed successfully\n")
                            return remove_line()
                        elif confirm == "no":
                            return remove_line()
                        else:
                            print(f"{RED}choice yes or no please !!{RESET}\n")
                else:
                    print(f"{RED}There is no line with name {line_name} !!{RESET}")

            else:
                print(f"{RED} there is no line yet!\n make a line first {RESET}")
                return emp_panel()
        elif choice == "2":
            return emp_panel()
        else:
            print(f"{RED}please enter 1 or 2 !!!{RESET} \n")


def show_lines():
    if len(lines.values()) != 0:
        for line in lines.values():
            print(line)
        print("\n" * 2)
        input(f"{BLUE}press Enter to back main menu{RESET}")
        return emp_panel()
    else:
        print(f"{RED}There is no line to show ! {RESET}")
        print(f"{RED}Make a line first ! {RESET}\n")
        return emp_panel()


def add_train():
    pass


def update_train():
    pass


def remove_train():
    pass


def show_trains():
    pass


def main_menu():
    pass


emp_panel()
