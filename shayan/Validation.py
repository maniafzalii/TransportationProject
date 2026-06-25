import re

RESET = '\033[0m'
RED = '\033[91m'

def validate_password(password):
    pattern = r"^(?=.*[@&])(?=.*[0-9])(?=.*[a-zA-Z]).*$"
    if re.match(pattern, password):
        return True

    else:
        print("Not Valid password , try again !!")
        return False

def validate_email(email):
    pattern = r".+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        print("not valid email ! try again")
        return False


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
    name = letter_please("Enter line name : ")
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


