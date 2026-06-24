from textwrap import dedent
import re

travelers_data = {}
tickets_data = {}


class Ticket:
    pass


class Traveler:
    def __init__(self, username):
        self.username = username


def validate_password(password):
    pattern = r"^(?=.*[@&])(?=.*[0-9])(?=.*[a-zA-Z])[a-zA-Z0-9@&]*$"
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


def traveler_panel():
    while True:
        user_input_traveler_panel = input(dedent("""
        1. Register
        2. Login
        3. Return to start menu
        -------------------------
        Your choice? """))
        match user_input_traveler_panel:

            case "1":
                traveler_register_menu()
            case "2":
                login_result = traveler_login_menu()
                if login_result:
                    purchase_panel(login_result)
            case "3":
                break
            case _:
                print("Invalid number")


def traveler_register_menu():
    print("Enter 0 anytime to return")
    traveler_register_name = input("Enter your name: ").strip()
    if traveler_register_name == "0":
        return

    while True:
        traveler_register_email = input("Enter your email: ").strip()
        if traveler_register_email == "0":
            return
        if traveler_register_email in [travelers_data[u]["email"] for u in travelers_data.keys()]:
            print("Someone already registered with this email!")
        elif validate_email(traveler_register_email):
            break

    while True:
        traveler_register_username = input("Enter your username: ").strip()
        if traveler_register_username == "0":
            return
        if traveler_register_username in travelers_data.keys():
            print("Username already exists!")
        else:
            break

    while True:
        traveler_register_password = input("Enter your password: ").strip()
        if traveler_register_password == "0":
            return
        if validate_password(traveler_register_password):
            break

    # add traveler data
    travelers_data[traveler_register_username] = {
        "name": traveler_register_name,
        "email": traveler_register_email,
        "password": traveler_register_password
        }
    print("Registered successfully!")


def traveler_login_menu():
    while True:
        print("Enter 0 anytime to return")
        traveler_login_username = input("Enter your username: ")
        if traveler_login_username == "0":
            return
        traveler_login_password = input("Enter your password: ")
        if traveler_login_password == "0":
            return
        if traveler_login_username in travelers_data.keys():
            if traveler_login_password == travelers_data[traveler_login_username]["password"]:
                print(f'Welcome {travelers_data[traveler_login_username]["name"]}!')
                return traveler_login_username
            else:
                print("Username and password does not match!")

        else:
            print("Username not found!")


def purchase_panel(traveler_username):
    purchase_panel_traveler = Traveler(traveler_username)
    while True:
        user_input_purchase_panel = input(dedent("""
        1. Buy ticket
        2. Edit your information
        3. Return to your panel
        -------------------------
        Your choice? """))
        match user_input_purchase_panel:
            case "1":
                pass
                # show trains list (destination, train_name, seats_remained, ticket_price, ...)
                # get train as input and buy it
                # purchase_panel_traveler.buy_ticket(train)
                # cannot buy more tickets than seats_remained
                # cannot buy tickets if wallet $$ < ticket_price
                # seats_remained -= tickets_bought
                # wallet $$ -= ticket_price
            case "2":
                pass
            case "3":
                return
            case _:
                print("Invalid number")

