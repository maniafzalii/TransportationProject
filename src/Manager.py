from src.Applicant import Applicant

from src.Employee import Employee

#subclass of Applicant it has list of employees as its own attribute
class Manager(Applicant):

    def __init__(self, user, password):
        super().__init__(user, password)    
        self.employees={}
    
    #validate username and password with manager to allow entrance
    def validate_entrance(self,username,password):
        if not(isinstance(username,str)) or not(isinstance(password,str)):
            raise TypeError("Username and Password must be String")
        return self.user==username and self.password==password
        
    #Where manager can control employees
    def manage_panel(self):

        ManagerMode=True
        print("----- You Enter as a Manager -----")
        while ManagerMode:
            print("----- Choose Your Action -----")
            print("1. Add Employee\n2. Remove Employee\n3. Show All Employees\n4. Exit Managing Pannel")
            try:
               ManagingAction=int(input())
            except ValueError:
               print("Invalid Input.Please Enter a number from [1,4] .")
               continue
            if ManagingAction==1:
                print("----- Enter Employee Information -----")
                username=input("Username ")
                password=input("Password ")
                name=input("Name ")
                family=input("Family ")
                email=input("Email ")
                try:
                    result=self.addEmployee(username,password,name,family,email)    
                    if result:
                       print("----- New Employee Added -----")
                    else: 
                       print("----- New Employee Not Added due to Repitition -----")
                except (ValueError,TypeError) as ex:
                    print(f"Error : {ex}")
            elif ManagingAction==2:
                print("----- Enter Username to Remove -----")
                username=input("Username ")
                try:
                    result=self.removeEmployee(username)
                    if result :
                       print(f"----- Employee {username} Removed -----")
                    else: 
                       print(f"----- Employee {username} Not Removed -----")
                except TypeError as ex:
                    print(f"Error : {ex}")       
            elif ManagingAction==3:
                self.showEployees()
            elif ManagingAction==4:
                print("----- Exit Manager Pannel -----")  
                ManagerMode=False
            else:
                print("----- Invalide Managing Action -----")   

            
          

    #firstly,create a new instance of employee if data is invalid raise error
    #then repitition is checked if there is equal employee return False
    #finally it is added to self.employees and return true
    def addEmployee(self,username,password,name,family,email):
        new_employee=Employee(username,password,name,family,email)
        if not self.employeeRepitionCheck(new_employee):
           return False
        self.employees[new_employee.user]=new_employee
        return True
        

    #remove emoployee by its username
    #is username not string raise error
    #if username is in self.employee retrun true otherwise return false
    def removeEmployee(self,username):
        if not isinstance(username,str):
            raise TypeError("Username must be String")
        if username in self.employees:
            self.employees.pop(username)
            return True
        return False
    
    #show list of employees 
    def showEployees(self):
        if len(self.employees)==0:
            print("Employee List is Empty")
            return
        idx=1
        for value in self.employees.values():
            print(f"{idx}. {value}")
            idx+=1

    


    #check if newemployee 's username or email exists in the self.employees or not
    def employeeRepitionCheck(self,newEmployee):
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

    #get username and password if employee is exist in list return true otherwise return false
    def validate_employee(self,username,password):
        if not(isinstance(username,str)) or not(isinstance(password,str)):
            raise TypeError("Username and Password must be String")
        for key,value in self.employees.items():
            if key==username and value.password==password:
                return True
        return False    
            
        
    #get username and return employee from employee list
    def get_Employee_By_Username(self,username):
        if not isinstance(username,str):
            raise TypeError("Username must be String")
        return self.employees[username] 

    #return list of employees
    def getEmployees(self):
        return self.employees