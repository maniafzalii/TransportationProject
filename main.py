from src.Traveler_src import *
<<<<<<< HEAD
from textwrap import dedent
from Applicant import Applicant
from Manager import Manager
from Employee import Employee
=======
from src.Manager import Manager
from textwrap import dedent
from shayan.Employee_panel import *
>>>>>>> 36123e6722efe9a05ea64ee143a37157ff25f774
# start panel


def main():

    print("----- Define Manager Username and Password -----")
    print("----- Be Carefull Username and Password can be contain alphabet,numbers,@,& -----")

    managerDefined=False
    while not managerDefined:
        try:
            username=input("Username: ").strip()
            password=input("Password: ").strip()
            manager=Manager(username,password)
            managerDefined=True
            print("----- Congrat, Manager is Defined -----")
        except (TypeError,ValueError) as ex:
            print(f"Error : {ex}")    
            print("Re-Enter Username and Password")
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
<<<<<<< HEAD
                managerValidated=False
                while not(managerValidated):
                    print("----- Enter Username and Password to Enter as Manager -----")
                    username=input("Username ").strip()
                    password=input("Password ").strip()
                    try:
                        result=manager.validate_entrance(username,password)
                        if result:
                           managerValidated=True
                        else:
                            print("----- Username or Password is Not Correct -----")
                            print("----- What is your next Action? -----")
                            print("1.Enter Entrance Data\n2.Exit Current Menu")
                            try:
                                mode=int(input())
                                if mode==1:
                                  continue
                                elif mode==2:
                                  break
                                else:
                                  print("Invalid input")
                            except ValueError as ex:
                                print(f"Error : {ex}")

                    except TypeError as ex:
                        print(f"Error : {ex}")        
                if managerValidated:
                    manager.manage_panel()
                 
            case "2":
                employeeValidated=False
                username=""
                while not(employeeValidated):
                    print("----- Enter Username and Password to Enter as Employee -----")
                    username=input("Username ").strip()
                    password=input("Password ").strip()
                    try:
                        result=manager.validate_employee(username,password)
                        if result:
                           employeeValidated=True
                        else:
                            print("----- Username or Password is not Correct -----")
                            print("----- What is your next Action? -----")
                            print("1.Enter Entrance Data\n2.Exit Current Menu")
                            try:
                                mode=int(input())
                                if mode==1:
                                  continue
                                elif mode==2:
                                  break
                                else:
                                  print("Invalid Input !")
                            except ValueError as ex:
                                print(f"Error : {ex}")

                    except TypeError as ex:
                        print(f"Error : {ex}")        
                if employeeValidated:
                    try:
                        employee=manager.get_Employee_By_Username(username)
                        if employee is None:
                          print("Employee Not Found!")
                        else:    
                            #SHAYAN call your panel
                            pass
                    except TypeError as ex:
                      print(f"Error : {ex}")

                 
=======
                pass
            case "2":
                emp_panel()
>>>>>>> 36123e6722efe9a05ea64ee143a37157ff25f774
            case "3":
                traveler_panel()
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid number")


if __name__ == "__main__":
    main()