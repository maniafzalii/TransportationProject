from textwrap import dedent
from shayan.Validation import *
from shayan.Train import *
from datetime import datetime


RED = '\033[91m'
BLUE = '\033[94m'
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
travelers_database = dict()
all_emails = list()


def card_validate(password, cvv2):
    if len(str(password)) != 6:
        return False
    if len(str(cvv2)) != 3:
        return False
    return True


def generate_payment_id(amount, card):
    import random
    return f'{card}{amount}{random.randint(100000, 999999)}'


class Card:
    def __init__(self, card, exp_month, exp_year, cvv2, password):
        self.card = card
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.password = password
        self.cvv2 = cvv2


    def __str__(self):
        return f"{self.card}"


class Traveler:
    def __init__(self, username, name, email, password, balance=0):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance
        self.cards = dict()
        self.transactions = list()
        self.tickets = list()


    def __str__(self):
        return f"username: {self.username}, name: {self.name}, email: {self.email}"


    def charge_wallet(self):
        print("Enter 0 anytime to return")

        while True:
            charge_amount_input = input("How much you want to charge? ").strip()
            if charge_amount_input == "0":
                return
            elif not charge_amount_input.isdigit():
                print("Invalid amount! Enter number")
                continue
            elif int(charge_amount_input) < 0:
                print("Invalid amount!")
                continue

            while True:
                charge_card_input = input("Enter card number: ").strip()
                if charge_card_input == "0":
                    break
                elif not charge_card_input.isdigit():
                    print("Invalid input!")
                    continue
                elif len(charge_card_input) != 16:
                    print("Must be 16 digits!")
                    continue

                charge_exp_month_input = input("Enter exp month: ").strip()
                if charge_exp_month_input == "0":
                    break
                elif not charge_exp_month_input.isdigit():
                    print("Enter number!")
                    continue
                elif not (1 <= len(charge_exp_month_input) <= 2):
                    print("Invalid number!")
                    continue
                elif not (1 <= int(charge_exp_month_input) <= 12):
                    print("Invalid number!")
                    continue

                charge_exp_year_input = input("Enter exp year: ").strip()
                if charge_exp_year_input == "0":
                    break
                elif not charge_exp_year_input.isdigit():
                    print("Invalid input!")
                    continue
                elif len(charge_exp_year_input) != 4:
                    print("Invalid number!")
                    continue
                elif int(charge_exp_year_input) < 1405 or int(charge_exp_year_input) > 1410:
                    print("Invalid year!")
                    continue

                charge_cvv2_input = input("Enter cvv2: ").strip()
                if charge_cvv2_input == "0":
                    break
                elif not charge_cvv2_input.isdigit():
                    print("Invalid input!")
                    continue

                charge_password_input = input("Enter password: ").strip()
                if charge_password_input == "0":
                    break
                elif not charge_password_input.isdigit():
                    print("Invalid number!")
                    continue

                if card_validate(int(charge_password_input), int(charge_cvv2_input)):
                    # card is ok and you charge now
                    current_card = Card(charge_card_input, charge_exp_month_input, charge_exp_year_input, charge_cvv2_input, charge_password_input)
                    self.cards[f"{charge_card_input}"] = current_card
                    payment_id = generate_payment_id(charge_amount_input, charge_card_input)
                    self.transactions.append(f'{GREEN} - [{datetime.now().strftime("%Y-%m-%d %H:%M")}]{RESET} Type: Charge | Amount: {charge_amount_input}T | Payment ID: {payment_id}')
                    self.balance += int(charge_amount_input)
                    print("Wallet charged successfully!")
                    return

                else:
                    print("Card information is not correct!!")



    def buy_ticket(self):
        print("Enter 0 anytime to return")
        while True:
            if not trains:
                print("No trains available")
                return

            if self.balance == 0:
                print("Please charge your wallet first!")
                return

            available_trains_to_buy = []
            for train in trains.values():
                if train.capacity == 0 or train.moveline == "Empty":
                    continue
                else:
                    available_trains_to_buy.append(train)
                    print(f"{BLUE} - {train}{RESET}")

            traveler_input_buy_ticket_id = input("Enter train ID to buy: ").strip()
            if traveler_input_buy_ticket_id == "0":
                return
            elif trains[traveler_input_buy_ticket_id] in available_trains_to_buy:
                train_to_buy = trains[traveler_input_buy_ticket_id]

                while True:
                    traveler_input_buy_ticket_capacity = int(input("How many tickets you wanna buy? ").strip())
                    if traveler_input_buy_ticket_capacity == "0":
                        break
                    elif train_to_buy.capacity < traveler_input_buy_ticket_capacity:
                        print(f"Not enough seats! only {train_to_buy.capacity} left.")
                    elif self.balance < (train_to_buy.ticket_price * traveler_input_buy_ticket_capacity):
                        print(f"Please charge your wallet {train_to_buy.ticket_price * traveler_input_buy_ticket_capacity - self.balance}T at least first!")
                        return
                    # buying process start
                    else:
                        while True:
                            print(f'{BLUE} - [{datetime.now().strftime("%Y-%m-%d %H:%M")}]{RESET} Train name: {train_to_buy.name} | Seats: {traveler_input_buy_ticket_capacity}x | Ticket price(x1): {train_to_buy.ticket_price} | Train stars: {train_to_buy.stars} | Train ID: {train_to_buy.id}')
                            final_check = input("Confirm purchase?(y/n) ").strip().lower()
                            if final_check == "n":
                                return
                            elif final_check == "y":
                                final_price = train_to_buy.ticket_price * traveler_input_buy_ticket_capacity
                                train_to_buy.capacity -= traveler_input_buy_ticket_capacity
                                self.tickets.append(f'{BLUE} - [{datetime.now().strftime("%Y-%m-%d %H:%M")}]{RESET} Train name: {train_to_buy.name} | Seats: {traveler_input_buy_ticket_capacity}x | Ticket price(x1): {train_to_buy.ticket_price} | Train stars: {train_to_buy.stars} | Train ID: {train_to_buy.id}')
                                self.balance -= final_price
                                payment_id = generate_payment_id(final_price, self.cards[0])
                                self.transactions.append(f'{GREEN} - [{datetime.now().strftime("%Y-%m-%d %H-%M")}]{RESET} Type: Shop | Amount: {final_price}T | Payment ID: {payment_id}')
                                print("Ticket purchased successfully. Have a good trip!!")
                                return
                            else:
                                print("Invalid input!")

            else:
                print("Train not found!")


    def edit_name(self):
        print("Enter 0 anytime to return")
        while True:
            traveler_input_edit_name = input("Enter your new name: ").strip()
            if traveler_input_edit_name == "0":
                return
            elif traveler_input_edit_name == self.name:
                print(f"Your name is already {self.name}")
            elif validate_name(traveler_input_edit_name):
                self.name = traveler_input_edit_name
                print(f"Name changed to '{self.name}'")
                return


    def edit_email(self):
        while True:
            traveler_input_edit_email = input("Enter your new email: ").strip()
            if traveler_input_edit_email == "0":
                return
            elif traveler_input_edit_email == self.email:
                print(f"Your email is already {self.email}")
            elif validate_email(traveler_input_edit_email):
                if traveler_input_edit_email in all_emails:
                    print("Someone already registered with this email!")
                else:
                    all_emails.remove(traveler_input_edit_email)
                    self.email = traveler_input_edit_email
                    all_emails.append(traveler_input_edit_email)
                    print(f"Email changed to '{self.email}'")
                    return


    def edit_password(self):
        while True:
            password_check = input("Enter your current password: ").strip()
            if password_check == "0":
                return
            elif password_check == self.password:
                while True:
                    traveler_input_edit_password = input("Enter your new password: ").strip()
                    if traveler_input_edit_password == "0":
                        return
                    elif traveler_input_edit_password == self.password:
                        print("You are already using that password!")
                    elif validate_password(traveler_input_edit_password):
                        self.password = traveler_input_edit_password
                        print("Password changed successfully")
                        return
            else:
                print("Incorrect password!")


def traveler_panel():
    while True:
        user_input_traveler_panel = input(dedent("""
        1. Register
        2. Login
        3. Return to start menu
        -------------------------
        Your choice? """)).strip()
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
    while True:
        traveler_register_name = input("Enter your name: ").strip()
        if traveler_register_name == "0":
            return
        elif validate_name(traveler_register_name):
            break

    while True:
        traveler_register_email = input("Enter your email: ").strip()
        if traveler_register_email == "0":
            return
        elif validate_email(traveler_register_email):
            if traveler_register_email in all_emails:
                print("Someone already registered with this email!")
            else:
                break

    while True:
        traveler_register_username = input("Enter your username: ").strip()
        if traveler_register_username == "0":
            return
        elif validate_username(traveler_register_username):
            if traveler_register_username in travelers_database.keys():
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
    all_emails.append(traveler_register_email)
    travelers_database[traveler_register_username] = Traveler(traveler_register_username, traveler_register_name, traveler_register_email, traveler_register_password)
    print("Registered successfully!")


def traveler_login_menu():
    print("Enter 0 anytime to return")
    while True:
        traveler_login_username = input("Enter your username: ").strip()
        if traveler_login_username == "0":
            return
        traveler_login_password = input("Enter your password: ").strip()
        if traveler_login_password == "0":
            return
        if traveler_login_username in travelers_database.keys():
            if traveler_login_password == travelers_database[traveler_login_username].password:
                print(f'Welcome {travelers_database[traveler_login_username].name}!')
                return travelers_database[traveler_login_username]
            else:
                print("Username and password does not match!")

        else:
            print("Username not found!")


def purchase_panel(traveler):
    while True:
        user_input_purchase_panel = input(dedent("""
        1. Buy ticket
        2. Wallet
        3. My tickets
        4. See your information
        5. Edit your information
        6. Log out
        -------------------------
        Your choice? """)).strip()
        match user_input_purchase_panel:
            case "1":
                traveler.buy_ticket()
            case "2":
                wallet_menu(traveler)
            case "3":
                if not traveler.tickets:
                    print("You do not have any tickets yet!")
                else:
                    for ticket in traveler.tickets:
                        print(ticket)
            case "4":
                print(traveler)
            case "5":
                edit_info_menu(traveler)
            case "6":
                return
            case _:
                print("Invalid number")


def edit_info_menu(traveler):
    while True:
        user_input_edit_info = input(dedent("""
        1. Edit name
        2. Edit email
        3. Edit password
        4. Return to your panel
        -------------------------
        Your choice? """)).strip()
        match user_input_edit_info:

            case "1":
                traveler.edit_name()
            case "2":
                traveler.edit_email()
            case "3":
                traveler.edit_password()
            case "4":
                return
            case _:
                print("Invalid number")


def wallet_menu(traveler):
    while True:
        user_input_wallet_menu = input(dedent(f"""
        Balance = {traveler.balance} T
        1. Charge wallet
        2. My cards
        3. Transactions
        4. Return to your panel
        -------------------------
        Your choice? """)).strip()
        match user_input_wallet_menu:

            case "1":
                traveler.charge_wallet()
            case "2":
                if not traveler.cards:
                    print("No cards added yet!")
                else:
                    for card in traveler.cards:
                        print(f"{YELLOW} - {card}{RESET}")
            case "3":
                if not traveler.transactions:
                    print("No transactions yet!")
                else:
                    for transaction in traveler.transactions:
                        print(transaction)
            case "4":
                return
            case _:
                print("Invalid number")