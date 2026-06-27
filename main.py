from src.Traveler_src import *
from textwrap import dedent
from src.Manager import Manager
from src.Employee import Employee
from textwrap import dedent
from shayan.Employee_panel import *

# start panel


def main():

    manager_username="team5"
    manager_password="@team5"
    manager=Manager(manager_username,manager_password)
    print("-------------------------------------------")
    print("----- Welcome to Transportation Panel -----")
    print("-------------------------------------------")
    while True:
        user_input_main = input(dedent("""
        ----- Choose Your Entrance Mode -----
        1. Manager
        2. Employee
        3. Traveler
        4. Exit
        -------------------------
        Your choice? """)).strip()

        match user_input_main:
            case "1":
                manager.enter_manager_panel()
                print("test")
            case "2":
                manager.enter_employee_panel()
            case "3":
                traveler_panel()
            case "4":
                print("----- GoodBye! -----")
                break
            case _:
                print("----- Invalid Entrance Mode ------")


if __name__ == "__main__":
    main()