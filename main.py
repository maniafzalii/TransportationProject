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

    print("\n-------------------------------------------")
    print("----- Welcome to Transportation Panel -----")
    print("-------------------------------------------\n")

    print(f"{GREEN}-------------------------------------------")
    print("----- Welcome to Transportation Panel -----")
    print(f"-------------------------------------------{RESET}")

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
            case "2":
                manager.enter_employee_panel()
            case "3":
                traveler_panel()
            case "4":
                print(f"{GREEN}----- GoodBye -----{RESET}")
                break
            case _:
                print(f"{RED}Invalid entrance mode.{RESET}")


if __name__ == "__main__":
    main()