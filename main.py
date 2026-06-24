from src.Traveler_src import *

# start panel

def main():
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