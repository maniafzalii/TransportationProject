from src.Applicant import Applicant
from textwrap import dedent
from src.Employee import Employee
from shayan.Employee_panel import emp_panel
#subclass of Applicant it has list of employees as its own attribute
class Manager(Applicant):

    def __init__(self, user, password):
        super().__init__(user, password)    
        self.employees={}
    
    def enter_manager_panel(self):
        manager_validated=False
        while not manager_validated:
            print("----- To Enter as a Manager : Enter Username and Password -----")
            print("----- Press 0 to Exit")
            username=input("Username ").strip()
            password=input("Password ").strip()
            if username=="0" or password=="0":
               print("----- Returning to previous menu -----")
               return
            try:
                result=self.validate_entrance(username,password)
                if result:
                  print("----- Login Successful.Welcome Manager Panel -----")
                  manager_validated=True
                  self.execute_manager_panel()
                else:
                    print("----- Username or Password is Wrong -----")  
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
                              print("----- Invalid Action -----")
            except TypeError as ex:
                print(f"----- Error : {ex} -----")     
        
      
    #validate username and password with manager to allow entrance
    def validate_entrance(self,username,password):
        if not(isinstance(username,str)) or not(isinstance(password,str)):
            raise TypeError("Username and Password must be String")
        return self.user==username and self.password==password
        
    #Where manager can control employees
    def execute_manager_panel(self):
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
                    print("----- Enter Employee Information -----")
                    username=input("Username ").strip()
                    password=input("Password ").strip()
                    name=input("Name ").strip()
                    family=input("Family ").strip()
                    email=input("Email ").strip()
                    try:
                        result=self.add_employee(username,password,name,family,email)
                        if result:
                            print("----- New Employee Added -----")
                        else:
                            print("----- New Employee Not Added due to Repitition -----")
                    except (ValueError,TypeError) as ex:
                        print(f">>>>> Error : {ex}")
                case "2":    
                    print("----- Enetr Username to Remove Employee -----")
                    username=input("Username ").strip()
                    try:
                        self.remove_employee(username)
                    except (ValueError,TypeError) as ex:
                        print(f">>>>> Error : {ex}")  
                case "3":
                    self.show_employees()
                case "4":
                    print("----- Exit Manager Panel -----")
                    ManagerMode=False   
                case _:
                    print("----- Invalid Managing Action -----")           
      

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
            raise TypeError("Username must be String")
        if not username in self.employees:
             raise ValueError("Employeee Not Found") 
        self.employees.pop(username)

    #show list of employees 
    def show_employees(self):

        if len(self.employees)==0:
            print("----- Employee List is Empty -----")
            return
        print("---------- Employee List ----------")
        idx=1
        for value in self.employees.values():
            print(f"{idx}. {value}")
            idx+=1

    


    #check if newemployee 's username or email exists in the self.employees or not
    #this method use by manager in add_employee method
    def employee_repition_check(self,newEmployee):
        if len(self.employees)==0:
            return True
        if newEmployee.user in self.employees:
            print(f"Username {newEmployee.user} exist !")
            return False
        for emp in self.employees.values():
            if emp.email==newEmployee.email:
               print(f"Email {newEmployee.email} exist !")
               return False
        return True
    
    def enter_employee_panel(self):
        employee_validated=False
        while not employee_validated:
            print("----- To Enter as an Employee : Enter Username and Password -----")
            print("----- Press 0 to Exit")
            username=input("Username ").strip()
            password=input("Password ").strip()
            if username=="0" or password=="0":
               print("----- Returning to previous menu -----")
               return

            try:
                result=self.validate_employee(username,password)
                if result:
                   print("----- Login Successful.Welcome Employee Panel -----")
                   employee_validated=True
                   emp_panel()
                else:
                    print("----- Username or Password is Wrong -----")  
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
                              print("----- Invalid Action -----")
            except TypeError as ex:
                print(f"----- Error : {ex} -----")     

    #get username and password 
    # if employee is exist in list return true otherwise return false
    def validate_employee(self,username,password):
        if not(isinstance(username,str)) or not(isinstance(password,str)):
            raise TypeError("Username and Password must be String")
        for key,value in self.employees.items():
            if key==username and value.password==password:
                return True
        return False    
            
        
    #get username and return employee from employee list
    def get_employee_by_username(self,username):
        if not isinstance(username,str):
            raise TypeError("Username must be String")
        return self.employees[username] 

    #return list of employees
    def get_employees(self):
        return self.employees