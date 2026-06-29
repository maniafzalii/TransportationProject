from textwrap import dedent
from shayan.Validation import validate_name, validate_email, validate_username, validate_password
from shayan.Train import trains
from datetime import datetime
import random


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
    return f'{card}{amount}{random.randint(100000, 999999)}'


class Card:
    def __init__(self, card, exp_month, exp_year, cvv2, password):
        self.card = card
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.password = password
        self.cvv2 = cvv2


    def __str__(self):
        return f"{self.card} | exp m: {self.exp_month} | exp year: {self.exp_year}"


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
        print("\nEnter 0 anytime to return")

        while True:
            charge_amount_input = input("How much you want to charge? ").strip()
            if charge_amount_input.isdigit():
                if int(charge_amount_input) == 0:
                    return
            else:
                print(f"{RED}Enter a positive number.{RESET}")
                continue
            charge_amount_input = int(charge_amount_input)

            while True:
                charge_card_input = input("Enter card number: ").strip()
                if charge_card_input.isdigit():
                    if int(charge_card_input) == 0:
                        break
                    elif len(charge_card_input) != 16:
                        print(f"{RED}Card must be a 16-digit number.{RESET}")
                        continue
                else:
                    print(f"{RED}Card must be a number.{RESET}")
                    continue

                charge_exp_month_input = input("Enter exp month: (1-12)").strip()
                if charge_exp_month_input.isdigit():
                    if int(charge_exp_month_input) == 0:
                        break
                    elif not (1 <= int(charge_exp_month_input) <= 12):
                        print(f"{RED}I guess you just invented a new month! Try 1–12.{RESET}")
                        continue
                else:
                    print(f"{RED}Month must be number.{RESET}")
                    continue

                charge_exp_year_input = input("Enter exp year:(1405-1410) ").strip()
                if charge_exp_year_input.isdigit():
                    if int(charge_exp_year_input) == 0:
                        break
                    elif len(charge_exp_year_input) != 4:
                        print(f"{RED}Year must be a 4-digit number.{RESET}")
                        continue
                    elif int(charge_exp_year_input) < 1405 or int(charge_exp_year_input) > 1410:
                        print(f"{RED}Your card appears to be expired! try again.{RESET}")
                        continue
                else:
                    print(f"{RED}Year must be number.{RESET}")
                    continue

                charge_cvv2_input = input("Enter cvv2: (3-digit number)").strip()
                if charge_cvv2_input.isdigit():
                    if int(charge_cvv2_input) == 0:
                        break
                    elif len(charge_cvv2_input) != 3:
                        print(f"{RED}cvv2 must be a 3-digit number.{RESET}")
                        continue
                else:
                    print(f"{RED}cvv2 must be a 3-digit number.{RESET}")
                    continue

                charge_password_input = input("Enter password(OTP): (6-digit number)").strip()
                if charge_password_input == "0":
                    break
                elif not charge_password_input.isdigit():
                    print(f"{RED}Password must be a 6-digit number.{RESET}")
                    continue
                elif len(charge_password_input) != 6:
                    print(f"{RED}Password must be a 6-digit number.{RESET}")
                    continue

                if card_validate(int(charge_password_input), int(charge_cvv2_input)):
                    # card is ok and you charge now
                    current_card = Card(charge_card_input, charge_exp_month_input, charge_exp_year_input, charge_cvv2_input, charge_password_input)
                    self.cards[charge_card_input] = current_card
                    payment_id = generate_payment_id(charge_amount_input, charge_card_input)
                    self.transactions.append(f'{GREEN} - [{datetime.now().strftime("%Y-%m-%d %H:%M")}]{RESET} Type: Charge | Amount: {int(charge_amount_input)}T | Payment ID: {payment_id}')
                    self.balance += int(charge_amount_input)
                    print(f"\n{BLUE}Wallet charged successfully.{RESET}")
                    return

                else:
                    print(f"{RED}Card information is not correct.{RESET}")



    def buy_ticket(self):
        if not trains:
            print(f"\n{YELLOW}No trains available.{RESET}")
            return

        print("Enter 0 anytime to return")

        while True:
            if self.balance == 0:
                match input("Your wallet is empty! You wanna charge?(y/n) ").strip().lower():
                    case "y":
                        self.charge_wallet()
                        continue
                    case "n":
                        pass
                    case _:
                        print(f"{RED}Invalid input.{RESET}")
                        continue

            available_trains_to_buy = []
            print()
            for train in trains.values():
                if train.capacity == 0 or train.moveline == "Empty":
                    continue
                else:
                    available_trains_to_buy.append(train)
                    print(f'{YELLOW}{" " * (5 - train.stars)}{"*" * train.stars}{RESET}{BLUE} | Train ID: {train.id} | Train name: {train.name} | Ticket price(1x): {int(train.ticket_price)}{RESET}')

            if not available_trains_to_buy:
                print(f"\n{YELLOW}No trains available to buy.{RESET}")
                return

            while True:
                traveler_input_buy_ticket_id = input("\nEnter train ID to buy: ").strip()
                if traveler_input_buy_ticket_id.isdigit():
                    if int(traveler_input_buy_ticket_id) == 0:
                        return
                else:
                    print(f"{RED}Enter a valid ID number.{RESET}")
                    continue

                try:
                    if trains[traveler_input_buy_ticket_id] in available_trains_to_buy:
                        train_to_buy = trains[traveler_input_buy_ticket_id]
                    else:
                        print(f"{RED}No trains available with this ID.{RESET}")
                        continue
                except KeyError:
                    print(f"{RED}No trains available with this ID.{RESET}")
                    continue

                while True:
                    traveler_input_buy_ticket_capacity = input("How many tickets you wanna buy? ").strip()
                    if not traveler_input_buy_ticket_capacity.isdigit():
                        print(f"{RED}Enter a number.{RESET}")
                        continue

                    traveler_input_buy_ticket_capacity = int(traveler_input_buy_ticket_capacity)
                    if traveler_input_buy_ticket_capacity == 0:
                        return
                    elif int(train_to_buy.capacity) < traveler_input_buy_ticket_capacity:
                        print(f"{RED}Not enough seats. only {int(train_to_buy.capacity)} left.{RESET}")
                        continue
                    elif self.balance < int(train_to_buy.ticket_price) * traveler_input_buy_ticket_capacity:
                        print(f"{RED}Please charge your wallet {int(train_to_buy.ticket_price) * traveler_input_buy_ticket_capacity - self.balance}T at least.{RESET}")
                        continue

                    else:
                        while True:
                            print(f'{YELLOW}{" " * (5 - train_to_buy.stars)}{"*" * train_to_buy.stars}{RESET}{BLUE} - Train name: {train_to_buy.name} | Seats: {traveler_input_buy_ticket_capacity}x | Ticket price(1x): {int(train_to_buy.ticket_price)} | Train ID: {train_to_buy.id}{RESET}')
                            final_check = input("Confirm purchase?(y/n) ").strip().lower()
                            if final_check == "n":
                                break

                            elif final_check == "y":
                                final_price = int(train_to_buy.ticket_price) * traveler_input_buy_ticket_capacity
                                train_to_buy.capacity -= traveler_input_buy_ticket_capacity
                                self.tickets.append(
                                    f'{BLUE} - [{datetime.now().strftime("%Y-%m-%d %H:%M")}]{RESET} {YELLOW}{" " * (5 - train_to_buy.stars)}{"*" * train_to_buy.stars}{RESET}{BLUE} - Train name: {train_to_buy.name} | Seats: {traveler_input_buy_ticket_capacity}x | Ticket price(1x): {int(train_to_buy.ticket_price)} | Train ID: {train_to_buy.id}{RESET}')
                                self.balance -= final_price
                                try:
                                    payment_id = generate_payment_id(final_price, list(self.cards.keys())[0])
                                except IndexError:
                                    payment_id = generate_payment_id(final_price, str(random.randint(5022000000000000, 8056000000000000)))
                                self.transactions.append(
                                    f'{GREEN} - [{datetime.now().strftime("%Y-%m-%d %H:%M")}]{RESET} Type: Shop | Amount: {final_price}T | Payment ID: {payment_id}')
                                print(f"{BLUE}Ticket purchased successfully. Have a good trip ;){RESET}")
                                return

                            else:
                                print(f"{RED}Invalid input{RESET}")


    def edit_name(self):
        print("\nEnter 0 anytime to return")
        while True:
            traveler_input_edit_name = input("Enter your new name: ").strip()
            if traveler_input_edit_name.isdigit():
                if int(traveler_input_edit_name) == 0:
                    return
                else:
                    print(f"{RED}Name must be a word.{RESET}")
            elif traveler_input_edit_name == self.name:
                print(f"{BLUE}Your name is already {self.name}.{RESET}")
            elif validate_name(traveler_input_edit_name):
                self.name = traveler_input_edit_name
                print(f"\n{BLUE}Name changed to '{self.name}'.{RESET}")
                return


    def edit_email(self):
        print("\nEnter 0 anytime to return")
        while True:
            traveler_input_edit_email = input("\nEnter your new email: ").strip()
            if traveler_input_edit_email.isdigit():
                if int(traveler_input_edit_email) == 0:
                    return
                else:
                    print(f"{RED}Not Valid Email {RESET} Correct Format is : {BLUE}username@domain.domain{RESET}\nTry Again\n")
            elif traveler_input_edit_email == self.email:
                print(f"{BLUE}Your email is already '{self.email}'.{RESET}")
            elif validate_email(traveler_input_edit_email):
                if traveler_input_edit_email in all_emails:
                    print(f"{RED}Someone has already registered with this email.{RESET}")
                else:
                    try:
                        all_emails.remove(self.email)
                    except ValueError:
                        pass
                    self.email = traveler_input_edit_email
                    all_emails.append(self.email)
                    print(f"\n{BLUE}Email changed to '{self.email}'.{RESET}")
                    return


    def edit_password(self):
        print("\nEnter 0 anytime to return")
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
                        print(f"{BLUE}You are already using that password.{RESET}")
                    elif validate_password(traveler_input_edit_password):
                        self.password = traveler_input_edit_password
                        print(f"{BLUE}Password changed successfully.{RESET}")
                        return
            else:
                print(f"{RED}Incorrect password.{RESET}")


def traveler_panel():
    while True:
        user_input_traveler_panel = input(dedent("""
        -------------------------
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
                print(f"{RED}Invalid number.{RESET}")


def traveler_register_menu():
    print("\nEnter 0 anytime to return")
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
                print(f"{RED}Someone already registered with this email.{RESET}")
            else:
                break

    while True:
        traveler_register_username = input("Enter your username: ").strip()
        if traveler_register_username.isdigit():
            if int(traveler_register_username) == 0:
                return

        if validate_username(traveler_register_username):
            if traveler_register_username in travelers_database.keys():
                print(f"{RED}Username already exists.{RESET}")
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
    print(f"\n{BLUE}Registered successfully.{RESET}")


def traveler_login_menu():
    print("\nEnter 0 anytime to return")
    while True:
        traveler_login_username = input("Enter your username: ").strip()
        if traveler_login_username == "0":
            return
        traveler_login_password = input("Enter your password: ").strip()
        if traveler_login_password == "0":
            return
        if traveler_login_username in travelers_database.keys():
            if traveler_login_password == travelers_database[traveler_login_username].password:
                print(f'\n{BLUE}Welcome {travelers_database[traveler_login_username].name}.{RESET}')
                return travelers_database[traveler_login_username]
            else:
                print(f"{RED}Username and password does not match.{RESET}")

        else:
            print(f"{RED}Username not found.{RESET}")


def purchase_panel(traveler):
    while True:
        user_input_purchase_panel = input(dedent("""
        -------------------------
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
                    print(f"{YELLOW}\nNO tickets yet.{RESET}")
                else:
                    for ticket in traveler.tickets:
                        print(ticket)
            case "4":
                print(f"\n{GREEN}{traveler}{RESET}")
            case "5":
                edit_info_menu(traveler)
            case "6":
                return
            case _:
                print(f"{RED}Invalid number.{RESET}")


def edit_info_menu(traveler):
    while True:
        user_input_edit_info = input(dedent("""
        -------------------------
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
                print(f"{RED}Invalid number.{RESET}")


def wallet_menu(traveler):
    while True:
        user_input_wallet_menu = input(dedent(f"""
        -------------------------
        {GREEN}Balance = {traveler.balance} T{RESET}
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
                    print(f"\n{YELLOW}No cards added yet.{RESET}")
                else:
                    print()
                    for card in traveler.cards.values():
                        print(f"{YELLOW} - {card}{RESET}")
            case "3":
                if not traveler.transactions:
                    print(f"\n{YELLOW}No transactions yet.{RESET}")
                else:
                    print()
                    for transaction in traveler.transactions:
                        print(transaction)
            case "4":
                return
            case _:
                print(f"{RED}Invalid number.{RESET}")
