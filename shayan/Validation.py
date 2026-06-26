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


def validate_name(name):
    if not name.isalpha():
        print(f"{RED}Name can only contain letters!{RESET}\n")
        return False
    if len(name) < 3 or len(name) > 15:
        print(f"{RED}Name must be between 3 and 15 characters.{RESET}\n")
        return False
    return True


def validate_username(username):
    if not username.isalnum():
        print("Username can only contain letters and numbers.")
        return False
    if len(username) < 3 or len(username) > 15:
        print("Username must be between 3 and 15 characters.")
        return False
    return True


def letter_please(prompt):
    while True:
        value = input(prompt).strip()
        if value.isalpha() == True or value == "0":
            return value
        else:
            print(f"{RED}use a-z A-Z as a correct input !{RESET}\n")


def number_please(prompt):
    while True:
        value = input(prompt)
        if value == "exit":
            return value
        else:
            if value.isdigit() == True:
                return int(value)
            else:
                print(f"{RED}use numbers only !!! {RESET}\n")





