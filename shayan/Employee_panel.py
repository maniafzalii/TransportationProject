from shayan.Train import *

class Line():
    def __init__(self, name: str, origin: str, destination: str, count: int, stations: list):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.count = count
        self.stations = stations

    def __str__(self):
        return f"line name:{BLUE} {self.name}{RESET}    origin: {self.origin}    destination:" \
               f" {self.destination}    number of stations: {self.count}    stations: {self.stations}"


lines = {}




BLUE = '\033[94m'
RESET = '\033[0m'
RED = '\033[91m'
GREEN = "\033[92m"


def emp_panel():
    print("1: Add new line\n2: Update line\n3: Remove line\n4: Show lines info\n"
          "5: Add Train\n6: Update Train info\n7: Remove Train\n8: Show Trains info\n"
          "9: Exit to main menu\n")
    choice = input(f"Please select an option ({BLUE}1-9{RESET}): ")
    if choice == "1":
        add_line()
    elif choice == "2":
        update_line()
    elif choice == "3":
        remove_line()
    elif choice == "4":
        show_lines()
    elif choice == "5":
        add_train()
    elif choice == "6":
        update_train()
    elif choice == "7":
        remove_train()
    elif choice == "8":
        show_trains()
    elif choice == "9":
        main_menu()
    else:
        print(f"{RED}Please select 1-9 !!!\n{RESET}")
        emp_panel()


def letter_please(prompt):
    while True:
        try:
            value = input(prompt).strip()

            if value == "0":
                return value
            if not value.isalpha():
                raise ValueError
            return value

        except ValueError:
            print(f"{RED}use a-z A-Z as a correct input !{RESET}\n")


def number_please(prompt):
    while True:
        try:
            value = input(prompt)

            if value == "exit":
                return value

            if value.strip().startswith("0"):
                print(f"{RED}Use Valid Numbers !!!{RESET}")
                continue

            if value.strip().startswith("-"):
                print(f"{RED}Don't use Negative Numbers !!! {RESET}\n")
                continue
            return int(value)

        except ValueError:
            print(f"{RED}Use numbers only !!! {RESET}\n")


def tname_please(prompt):
    while True:
        value = input(prompt).strip()

        if value == "0":
            return value

        if value and all(char.isalpha() or char.isdigit() or char in "-_ " for char in value):
            return value

        print(f"{RED}Use only letters, numbers, space, - or _ as a correct input!{RESET}\n")


def add_line():
    stations = []
    print(f"\n---{BLUE} Adding new line{RESET} ---\n")
    while True:
        name = letter_please(f"[0] back {BLUE}|{RESET} Enter line name : ")
        if name == "0":
            print(f"{BLUE}\nEmployee Menu {RESET}\n")
            return emp_panel()
        elif name in lines.keys():
            print(f"{RED}This line is already exist !!!\n {RESET}")
        else:
            break
    while True:
        origin = letter_please(f"[0] back {BLUE}|{RESET} Enter Origin city : ")
        if origin == "0":
            print(f"{BLUE}\nEmployee Menu {RESET}\n")
            return emp_panel()
        else:
            break
    while True:
        destination = letter_please(f"[0] back {BLUE}|{RESET} Destination city : ")
        if destination == "0":
            print(f"{BLUE}\nEmployee Menu {RESET}\n")
            return emp_panel()
        else:
            break
    while True:
        count = number_please(f"Enter {RED}exit{RESET} for back {BLUE}|{RESET} Enter the number of Stations : ")
        if count == "exit":
            print(f"{BLUE}\nEmployee Menu {RESET}\n")
            return emp_panel()
        else:
            break
    print(f"you have {count} stations ")
    i = 1
    while i <= count:
        station = letter_please(f"[0] back {BLUE}|{RESET} Enter station {i} name : ")
        if station == "0":
            print(f"{BLUE}\nEmployee Menu {RESET}\n")
            return emp_panel()
        else:
            if station not in stations:
                stations.append(station)
                i += 1
            else:
                print(f"{RED}this station is already exist !{RESET}")

    new_line = Line(name, origin, destination, count, stations)
    lines[name] = new_line
    print(f"\nNew line successfully added\n{BLUE}{new_line}{RESET}, \n")
    return emp_panel()


def update_line():
    choise = input(f"Select [1] for update{BLUE} | {RESET}Select [2] for exit : ")
    if choise == "1" and len(lines.keys()) != 0:

        while True:
            line_name = input(f"[0] back {BLUE}|{RESET} Enter line name please: ")
            if line_name == "0":
                return update_line()
            else:
                pass
            if line_name in lines.keys():
                print("")
                print(lines[line_name])
                while True:
                    choise = input(
                        "choose an option to change :\n"
                        " 1:name\n"
                        " 2:origin\n"
                        " 3:destination\n"
                        " 4:stations\n"
                        " 5:exit\n ==>    ")

                    if choise == "1":

                        while True:
                            new_name = letter_please(f"[0] back {BLUE}|{RESET} Enter line name: ")
                            if new_name == "0":
                                break
                            else:
                                if new_name in lines.keys():
                                    print(f"{RED}This line is already exist !!!\n {RESET}")
                                else:
                                    old_name = line_name

                                    lines[old_name].name = new_name
                                    lines[new_name] = lines.pop(old_name)
                                    for train in trains.values():
                                        if train.moveline == old_name:
                                            train.moveline = new_name
                                    line_name = new_name

                                    print(f"Name updated successfully: {old_name} to{GREEN} {new_name}{RESET}\n")
                                    break

                    elif choise == "2":
                        new_origin = letter_please(f"[0] back {BLUE}|{RESET} Origin city: ")
                        if new_origin == "0":
                            continue
                        else:
                            print(f"Origin updated successfully: {lines[line_name].origin} to{GREEN} {new_origin}{RESET}\n")
                            lines[line_name].origin = new_origin

                    elif choise == "3":
                        new_destination = letter_please(f"[0] back {BLUE}|{RESET} Destination city: ")

                        if new_destination == "0":
                            continue
                        else:
                            print(
                                f"Destination updated successfully: {lines[line_name].destination} to{GREEN} {new_destination}{RESET}\n")
                            lines[line_name].destination = new_destination

                    elif choise == "4":
                        new_count = number_please(
                            f"Enter{RED} exit{RESET} for back {BLUE}|{RESET} Enter the number of Stations: ")
                        if new_count == "exit":
                            continue
                        else:
                            new_stations = []
                            print(f"you have {new_count} stations ")
                            i = 1
                            while i <= new_count:
                                station = letter_please(f"[0] back {BLUE}|{RESET} Enter station {i} name: ")
                                if station == "0":
                                    break
                                else:
                                    if station not in new_stations:
                                        new_stations.append(station)
                                        i += 1
                                    else:
                                        print(f"{RED}This station is already exist !{RESET}")
                            print(f"Stations updated successfully: {lines[line_name].stations} to{GREEN} {new_stations}{RESET}")
                            lines[line_name].count = new_count
                            lines[line_name].stations = new_stations

                    elif choise == "5":
                        return update_line()
                    else:
                        print(f"{RED}select a number correctly !!{RESET}")
            else:
                print(f"{RED}There no line with name {line_name}{RESET}\n")
                return update_line()

    elif choise == "1" and len(lines.keys()) == 0:
        print(f"{RED}There is no line yet - go Add a line first !!{RESET}")
        return emp_panel()

    elif choise == "2":
        return emp_panel()

    else:
        print(f"{RED}Select carefully !!{RESET}")
        return update_line()


def remove_line():
    while True:
        choice = input("Enter [1] for removing lines or enter [2] and back to main menu : ")
        if choice == "1":
            if len(lines.keys()) != 0:
                print(f"\n---{BLUE}Removing Line{RESET}---\n")
                line_name = letter_please(f"[0] back {BLUE}|{RESET} Enter line name : ")
                if line_name == "0":
                    continue
                else:
                    if line_name in lines.keys():
                        while True:
                            confirm = input(f"Are you sure to remove line??\n {lines[line_name]} (yes/no) : ").lower()
                            if confirm == "yes":
                                for train in trains.values():
                                    if train.moveline == line_name:
                                        train.moveline = "Empty"
                                    else:
                                        pass
                                lines.pop(line_name)
                                print(f"{line_name} Removed successfully\n")
                                return remove_line()
                            elif confirm == "no":
                                return remove_line()
                            else:
                                print(f"{RED}choice yes or no please !!{RESET}\n")
                    else:
                        print(f"{RED}There is no line with name {line_name} !!{RESET}")

            else:
                print(f"{RED}There is no line yet!\n Add a line first {RESET}")
                return emp_panel()
        elif choice == "2":
            print(f"{BLUE}\nEmployee Menu {RESET}\n")
            return emp_panel()
        else:
            print(f"{RED}Please enter 1 or 2 !!!{RESET} \n")


def show_lines():
    if len(lines.values()) != 0:
        for line in lines.values():
            print(line)
        print("\n")
        input(f"{BLUE}Press Any key to back main menu\n{RESET}")
        return emp_panel()
    else:
        print(f"{RED}There is no line to show ! {RESET}")
        print(f"{RED}Add a line first ! {RESET}\n")
        return emp_panel()


def add_train():
    global train_id
    if len(lines.keys()) == 0:
        print(f"{RED}There is no line yet , Add line First !!{RESET}\n")
        return emp_panel()
    else:
        pass
    print(f"\n---{BLUE}Adding Train{RESET}---\n")
    name = tname_please(f"[0] back {BLUE}|{RESET} Enter Train name : ")
    if name == "0":
        print(f"{BLUE}\nEmployee Menu {RESET}\n")
        return emp_panel()
    else:
        pass
    while True:
        move_line = letter_please(f"[0] back {BLUE}|{RESET} Enter Train Line_name : ")
        if move_line == "0":
            return add_train()
        else:
            if move_line not in lines.keys():
                print(f"{RED}There is no line with name : {RESET}{BLUE}{move_line}{RESET}\n{RED}Try Again !{RESET}\n")
            else:
                break
    while True:
        speed = number_please(
            f"Enter{RED} exit{RESET} and back to main menu {BLUE}|{RESET} Trains average speed as Km/h : ")
        if speed == "exit":
            return add_train()
        if speed <= 10:
            print(f"{RED}To Sloooooow !!!!!!\nSpeed must bigger than 10 !!! {RESET}\n")
        elif speed > 300:
            print(f"{RED}Warni!!!!!!!ng\nTo Fast !!!!\nspeed must between 10 and 300{RESET}\n")
        else:
            break

    waiting_time = number_please(
        f"Enter{RED} exit {RESET}and back to manu {BLUE}|{RESET} Enter Waiting time in stations as minute? : ")
    if waiting_time == "exit":
        return add_train()
    else:
        pass
    while True:
        star = number_please(
            f"Enter{RED} exit {RESET} and back to manu {BLUE}|{RESET} Enter Train quality as a number : ")
        if star == "exit":
            return add_train()
        else:
            if 0 <= star <= 5:
                break
            else:
                print(f"{RED}Stars must be Digit between 0 - 5 !!! {RESET}\n")
    while True:
        ticket_price = number_please(
            f"Enter{RED} exit {RESET} and back to manu {BLUE}|{RESET} Enter Ticket_price like 100 - 200 -... : ")
        if ticket_price == "exit":
            return add_train()
        elif ticket_price > 10000:
            print(f"{RED}To Expensive ! ticket_price can't bigger than 10000 !!{RESET}\n")
        elif ticket_price <= 0:
            print(f"{RED}Ticket Can't be Free !! {RESET}\n")
        else:
            break
    while True:
        capacity = number_please(f"Enter{RED} exit {RESET} and back to manu {BLUE}|{RESET} Enter Train Capacity : ")
        if capacity == "exit":
            return add_train()
        elif capacity < 50:
            print(f"{RED}We are better take a taxi or bus\nCapacity must bigger than 50 !!! {RESET}\n")
        elif capacity > 2000:
            print(f"{RED}We can't get Train like This\nCapacity must lower than 2001 !! {RESET}\n")
        else:
            break

    new_train = Train(name, move_line, speed, waiting_time, star, ticket_price, capacity, train_id)
    trains[f"{train_id}"] = new_train
    train_id += 1
    print(f"new Train successfully added : \n{GREEN} new_train{RESET} \n")
    return emp_panel()


def update_train():
    choise = input("Select [1] for update or Select [2] for exit : ")

    if choise == "1" and len(trains.keys()) != 0:
        print("")
        while True:
            id_train = number_please(f"Enter {RED}exit{RESET} for back {BLUE}|{RESET} Enter Train ID: ")
            if id_train == "exit":
                return update_train()
            id_train = str(id_train)
            if id_train in trains.keys():
                print(trains[id_train])

                while True:
                    choise = input(
                        "choose an option to change :\n"
                        "1:name\n"
                        "2:line\n"
                        "3:speed\n"
                        "4:waiting time\n"
                        "5:stars\n"
                        "6:ticket price\n"
                        "7:capacity\n"
                        "8:exit\n ==>    ")

                    if choise == "1":
                        new_name = tname_please(f"[0] back {BLUE}|{RESET} Enter Train name: ")

                        if new_name == "0":
                            continue

                        print(
                            f"Train name updated successfully: {trains[id_train].name} to{GREEN} {new_name}{RESET}\n")

                        trains[id_train].name = new_name

                    elif choise == "2":

                        while True:
                            new_line = letter_please(f"[0] back {BLUE}|{RESET} Enter Train Line_name: ")

                            if new_line == "0":
                                break

                            if new_line not in lines.keys():
                                print(f"{RED}There is no line with name: {new_line}{RESET}")

                            else:
                                print(f"Train line updated successfully: {trains[id_train].moveline} to{GREEN} {new_line}{RESET}")

                                trains[id_train].moveline = new_line
                                break

                    elif choise == "3":
                        while True:
                            new_speed = number_please(f"Enter{RED} exit{RESET} for back {BLUE}|{RESET} Enter speed: ")
                            if new_speed == "exit":
                                break

                            if new_speed <= 10:

                                print(f"{RED}Speed must bigger than 10 !!!{RESET}")

                            elif new_speed > 300:
                                print(
                                    f"{RED}Speed must lower than 300 !!!{RESET}")

                            else:
                                print(f"Speed updated successfully: {trains[id_train].speed} to{GREEN} {new_speed}{RESET}\n")
                                trains[id_train].speed = new_speed
                                break

                    elif choise == "4":
                        new_waiting_time = number_please(
                            f"Enter{RED} exit{RESET} for back {BLUE}|{RESET} Enter waiting_time:  ")

                        if new_waiting_time == "exit":
                            continue

                        print(
                            f"Waiting time updated successfully: {trains[id_train].waiting_time} to{GREEN} {new_waiting_time}{RESET}")
                        trains[id_train].waiting_time = new_waiting_time

                    elif choise == "5":
                        while True:
                            new_star = number_please(f"Enter{RED} exit{RESET} for back {BLUE}|{RESET} Enter stars: ")

                            if new_star == "exit":
                                break

                            if 0 <= new_star <= 5:

                                print(f"Stars updated successfully: {trains[id_train].stars} to{GREEN} {new_star}{RESET}")
                                trains[id_train].stars = new_star
                                break
                            else:
                                print(f"{RED}Stars must be between 0 and 5 !{RESET}")

                    elif choise == "6":

                        while True:
                            new_ticket_price = number_please(
                                f"Enter{RED} exit{RESET} for back {BLUE}|{RESET} Enter ticket price: ")
                            if new_ticket_price == "exit":
                                break

                            if new_ticket_price <= 0:
                                print(f"{RED}Ticket can't be free !{RESET}")

                            elif new_ticket_price > 10000:
                                print(f"{RED}Ticket price can't bigger than 10000 !{RESET}")

                            else:
                                print(
                                    f"Ticket price updated successfully: {trains[id_train].ticket_price} to{GREEN} {new_ticket_price}{RESET}")

                                trains[id_train].ticket_price = new_ticket_price
                                break

                    elif choise == "7":

                        while True:
                            new_capacity = number_please(
                                f"Enter{RED} exit{RESET} for back {BLUE}|{RESET} Enter capacity: ")

                            if new_capacity == "exit":
                                break

                            if new_capacity < 50:
                                print(f"{RED}Capacity must bigger than 50 !{RESET}")

                            elif new_capacity > 2000:
                                print(f"{RED}Capacity must lower than 2001 !{RESET}")

                            else:
                                print(f"Capacity updated successfully: {trains[id_train].capacity} to{GREEN} {new_capacity}{RESET}")

                                trains[id_train].capacity = new_capacity
                                break

                    elif choise == "8":
                        return update_train()

                    else:
                        print(f"{RED}Select a number correctly !!{RESET}")

            else:
                print(f"{RED}There is no Train with ID: {id_train}{RESET}")

    elif choise == "1" and len(trains.keys()) == 0:

        print(f"{RED}There is no Train yet - Add Train First !!{RESET}")
        return emp_panel()

    elif choise == "2":
        print(f"{BLUE}\nEmployee Menu {RESET}\n")
        return emp_panel()

    else:
        print(f"{RED}Select carefully !!{RESET}")
        return update_train()


def remove_train():
    while True:
        choice = input("Enter [1] for removing Train or enter [2] and back to main menu : ")
        if choice == "1":
            if len(trains.keys()) != 0:
                print(f"\n---{BLUE}Removing Train{RESET}---\n")
                id_train = number_please(
                    f"Enter {RED}exit{RESET} and back to main menu {BLUE}|{RESET} Enter Train ID: ")
                if id_train == "exit":
                    continue
                else:
                    id_train = str(id_train)
                    if id_train in trains.keys():
                        while True:
                            confirm = input(f"Are you sure to remove Train??\n {trains[id_train]} (yes/no):  ").lower()
                            if confirm == "yes":
                                trains.pop(id_train)
                                print(f"Train with ID: {id_train}Rremoved successfully\n")
                                return remove_train()
                            elif confirm == "no":
                                return remove_train()
                            else:
                                print(f"{RED}Write yes or no please !!{RESET}\n")
                    else:
                        print(f"{RED}There is no Train with ID: {id_train} !!{RESET}")

            else:
                print(f"{RED} there is no Train yet!\n Add a Train first {RESET}")
                return emp_panel()
        elif choice == "2":
            return emp_panel()
        else:
            print(f"{RED}please enter 1 or 2 !!!{RESET} \n")


def show_trains():
    if len(trains.values()) != 0:
        for train in trains.values():
            print(train)
        print("\n")
        input(f"{BLUE}Press Any key to back main menu\n{RESET}\n")
        print(f"{BLUE}\nEmployee Menu {RESET}\n")
        return emp_panel()
    else:
        print(f"{RED}There is no Train to show ! {RESET}")
        print(f"{RED}Add a Train first ! {RESET}\n")
        return emp_panel()


def main_menu():
    pass

emp_panel()