from src.Applicant import Applicant
from textwrap import dedent
from src.Employee import Employee
from shayan.Employee_panel import emp_panel



BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
YELLOW = '\033[93m'

#subclass of Applicant it has list of employees as its own attribute
class Manager(Applicant):

    def __init__(self, user, password):
        super().__init__(user, password)    
        self.employees={}
    
    def enter_manager_panel(self):

        manager_validated=False
        while not manager_validated:
            #recieve username and password to enter as a manager
            #empty input is not acceptable,press 0 back to entrance mode
            print("\n----- To Enter as a Manager : Enter Username and Password -----\n")
            print("----- In Each Step Press 0 to Exit\n")
            username=input("Username ").strip()
            if username=="0":
               print("\n----- Returning to Previous Menu -----\n")
               return
            if len(username)==0:
               print(f"\n{RED}----- Username Can Not be Empty -----{RESET}\n")
               continue 
            password=input("Password ").strip()
            if password=="0":
               print("\n----- Returning to Previous Menu -----\n")
               return
            if len(password)==0:
               print(f"\n{RED}----- Password Can Not be Empty -----{RESET}\n")
               continue 
            try:
                #compare input with username and password of manager
                result=self.validate_entrance(username,password)
                if result:
                   #if username and password are correct ,user enter manager panel
                  print(f"\n{BLUE}----- Login Successful Welcome to Manager Panel -----{RESET}\n")
                  manager_validated=True
                  self.execute_manager_panel()
                else:
                    #if input is worng,ask user to choose next action
                    print(f"\n{RED}----- Username or Password is Wrong -----{RESET}\n")  
                    while True:
                        user_input=input(dedent("""\
                        ----- Choose Your Next Action -----
                        1. Enter Username,Password again
                        2. Exit
                        >>>>>  """)).strip()
                        match user_input:
                            case "1":
                              break
                            case "2":
                              return
                            case _:
                              print(f"\n{RED}----- Invalid Action -----{RESET}\n")
            except TypeError as ex:
                print(f"{RED}----- Error : {ex} -----{RESET}\n")     
        
      
    #validate username and password with manager to allow entrance
    def validate_entrance(self,username,password):
        #if input is not instance of string raise error
        if not(isinstance(username,str)) or not(isinstance(password,str)):
            raise TypeError(f"{RED}Username and Password must be String !{RESET}")
        return self.user==username and self.password==password
        
    #Where manager can control employees
    def execute_manager_panel(self):
        #while managrmode is true ,manager panel is running
        ManagerMode=True

        while ManagerMode:
            user_input=input(dedent("""\
                    ----- Choose Your Action -----
                    1. Add Employee 
                    2. Remove Employee
                    3. Show Employees
                    4. Exit Admin Panel
                    >>>>>  """)).strip()       
            match user_input:
                case "1":
                    print("\n----- Enter Employee Information -----\n")
                    print("----- In Each Step Press 0 to Exit\n")
                    username=input("Username ").strip()
                    if(username=="0"):
                        print("\n----- Returning to previous menu -----\n")
                        continue
                    if(len(username)==0):
                        print(f"\n{RED}----- Username Can Not be Empty -----{RESET}\n")
                        continue

                    password=input("Password ").strip()
                    if(password=="0"):
                        print("\n----- Returning to previous menu -----\n")
                        continue
                    if(len(password)==0):
                        print(f"\n{RED}----- Password Can Not be Empty -----{RESET}\n")
                        continue
                    name=input("Name ").strip()
                    if(name=="0"):
                        print("\n----- Returning to previous menu -----\n")
                        continue
                    if(len(name)==0):
                        print(f"\n{RED}----- Name Can Not be Empty -----{RESET}\n")
                        continue
                    family=input("Family ").strip()
                    if(family=="0"):
                        print("\n----- Returning to previous menu -----\n")
                        continue
                    if(len(family)==0):
                        print(f"\n{RED}----- Family Can Not be Empty -----{RESET}\n")
                        continue
                    email=input("Email ").strip()
                    if(email=="0"):
                        print("\n----- Returning to previous menu -----\n")
                        continue
                    if(len(email)==0):
                        print(f"\n{RED}----- E-mail Can Not be Empty -----{RESET}\n")
                        continue
                    try:
                        #add_employee return true or false or raise error
                        result=self.add_employee(username,password,name,family,email)
                        if result:
                            print(f"{BLUE}----- New Employee Added -----{RESET}\n")
                        else:
                            print(f"{RED}----- New Employee Not Added due to Repitition -----{RESET}\n")
                    except (ValueError,TypeError) as ex:
                        print(f"{RED}>>>>> Error : {ex}{RESET}\n")
                case "2":    
                    print("\n----- Enetr Username to Remove Employee -----\n")
                    username=input("Username ").strip()
                    if(username=="0"):
                        print("\n----- Returning to previous menu -----\n")
                        continue
                    if(len(username)==0):
                        print(f"{RED}\n----- Username Can Not be Empty -----{RESET}\n")
                        continue
                    try:
                        #remove employee, if list is empty or username not exist raise error
                        #if username not string raise error
                        self.remove_employee(username)
                    except (ValueError,TypeError) as ex:
                        print(f"{RED}>>>>> Error : {ex}{RESET}\n")  
                case "3":
                    self.show_employees()
                case "4":
                    print("\n----- Exit Manager Panel -----\n")
                    ManagerMode=False   
                case _:
                    print(f"\n{RED}----- Invalid Managing Action -----{RESET}\n")           
      

    #firstly,create a new instance of employee if data is invalid raise error
    #then repitition is checked if there is equal employee return False
    #finally it is added to self.employees and return true
    def add_employee(self,username,password,name,family,email):
        new_employee=Employee(username,password,name,family,email)
        if not self.employee_repition_check(new_employee):
           return False
        self.employees[new_employee.user]=new_employee
        return True
        

    #remove emoployee by its username
    #is username not string raise error
    #if username is not in self.Employees  or self.Employees is empty raise ValueError
    #otherwise remove employee
    def remove_employee(self,username):
        if not isinstance(username,str):
            raise TypeError(f"{RED}Username must be String !{RESET}")
        if not username in self.employees:
             raise ValueError(f"{RED}Employeee Not Found {RESET}") 
        self.employees.pop(username)
        print(f"{BLUE}----- Employee {username} Removed Successfully ----{RESET}\n ")

    #show list of employees 
    def show_employees(self):

        if len(self.employees)==0:
            print(f"{YELLOW}----- Employee List is Empty -----{RESET}\n")
            return
        print(f"{GREEN}---------- Employee List ----------{RESET}\n")
        print(f"{GREEN}Username        Password         Name         Family           E-mail{RESET}\n")
        idx=1
        for value in self.employees.values():
            print(f"{GREEN}{idx}. {value}{RESET}\n")
            idx+=1

    


    #check if newemployee 's username or email exists in the self.employees or not
    #this method use by manager in add_employee method
    def employee_repition_check(self,newEmployee):
        #if list is empty ,any user can add 
        if len(self.employees)==0:
            return True
        #first check username repitition then email repitition
        if newEmployee.user in self.employees:
            print(f"{RED}Username {newEmployee.user} exist !{RESET}\n")
            return False
        for emp in self.employees.values():
            if emp.email==newEmployee.email:
               print(f"{RED}Email {newEmployee.email} exist !{RESET}\n")
               return False
        return True
    #First examine existance of employee 
    def enter_employee_panel(self):
        employee_validated=False
        while not employee_validated:
            print("\n----- To Enter as an Employee : Enter Username and Password -----\n")
            print("----- In Each Step Press 0 to Exit")
            #recieve username and password to enter as a manager
            #empty input is not acceptable,press 0 back to entrance mode
            username=input("Username ").strip()
            if(username=="0"):
               print("\n----- Returning to previous menu -----\n")
               return 
            if(len(username)==0):
                print(f"\n{RED}----- Username Can Not be Empty -----{RESET}\n")
                continue
            password=input("Password ").strip()
            if  password=="0":
               print("\n----- Returning to previous menu -----\n")
               return
            if(len(password)==0):
                print(f"\n{RED}----- Password Can Not be Empty -----{RESET}\n")
                continue

            try:
                #examin existance of employee
                result=self.validate_employee(username,password)
                if result:
                   #call employee panel(emp_panel()) 
                   print(f"\n{BLUE}----- Login Successful Welcome to Employee Panel -----{RESET}\n")
                   employee_validated=True
                   emp_panel()
                else:
                    #ask user what is next action
                    print(f"\n{RED}----- Username or Password is Wrong -----{RESET}\n")  
                    while True:
                        user_input=input(dedent("""\
                        ----- Choose Your Next Action -----
                        1. Enter Username,Password again
                        2. Exit
                        >>>>>  """)).strip()
                        match user_input:
                            case "1":
                              break
                            case "2":
                              return
                            case _:
                              print(f"{RED}----- Invalid Action -----{RESET}\n")
            except TypeError as ex:
                print(f"{RED}----- Error : {ex} -----{RESET}")     

    #get username and password 
    # if employee is exist in list return true otherwise return false
    def validate_employee(self,username,password):
        if not(isinstance(username,str)) or not(isinstance(password,str)):
            raise TypeError(f"{RED}Username and Password must be String !{RESET}")
        for key,value in self.employees.items():
            if key==username and value.password==password:
                return True
        return False    
            
        
    #get username and return employee from employee list
    def get_employee_by_username(self,username):
        if not isinstance(username,str):
            raise TypeError(f"{RED}Username must be String !{RESET}")
        return self.employees[username] 

    #return list of employees
    def get_employees(self):
        return self.employees