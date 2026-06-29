import re

RESET = '\033[0m'
RED = '\033[91m'
BLUE = '\033[94m'


def validate_password(password):
    pattern = r"^(?=.*[@&])(?=.*[0-9])(?=.*[a-zA-Z]).*$"
    if re.match(pattern, password):
        return True

    else:
        print(
            f"{RED}Not Valid Password{RESET} Password must contain {BLUE}[number and word and symbol [@&] !{RESET}\nTry Again\n ")
        return False


def validate_email(email):
    pattern = r".+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        print(f"{RED}Not Valid Email {RESET} Correct Format is : {BLUE}username@domain.domain{RESET}\nTry Again\n")
        return False


def validate_name(name):
    if not name.isalpha():
        print(f"{RED}Name can only contain letters!{RESET}\n")
        return False
    if len(name) < 2 or len(name) > 20:
        print(f"{RED}Name must be between 2 and 20 characters.{RESET}\n")
        return False
    return True


def validate_username(username):
    if len(username) < 3 or len(username) > 20:
        print("Username must be between 3 and 20 characters.")
        return False
    return True


def letter_please(prompt):
    while True:
        try:
            value = input(prompt).strip()

            if value == "0":
                return value
            if not (value.isalnum() and any(c.isalpha() for c in value)):
                raise ValueError
            return value

        except ValueError:
            print(f"{RED}Use letters or text-number combinations as a correct input !{RESET}\n")


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
