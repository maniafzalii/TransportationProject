from src.Traveler_src import *
from src.Manager import Manager
from textwrap import dedent
# start panel


def main():

    print("----- Define Manager Username and Password -----")
    print("----- Be Carefull Username and Password can be contain alphabet,numbers,@,& -----")

    managerDefined=True
    username=input("Username ")
    password=input("Password ")
    manager=Manager(username,password)
    while managerDefined:
        if(manager.user is None)or( manager.password is None):
           print("Re Enter Username and Password")
           username=input("Username ")
           password=input("Password ")
           manager=Manager(username,password)
        else:
           managerDefined=False
    while True:
        user_input_main = input(dedent("""
        Welcome!
        1. Admin
        2. Employee
        3. Traveler
        4. Exit
        -------------------------
        Your choice? """)).strip()

        match user_input_main:
            case "1":
                pass
            case "2":
                pass
            case "3":
                traveler_panel()
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid number")


if __name__ == "__main__":
    main()