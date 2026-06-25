from Applicant import Applicant

from Employee import Employee

#subclass of Applicant it has list of employees as its own attribute
class Manager(Applicant):

    def __init__(self, user, password):
        super().__init__(user, password)    
        self.employees=[]
    
    def manage_panel(self):
        ManagerMode=True
        print("----- You Enter as a Manager -----")
        while ManagerMode:
            print("----- Choose Your Action -----")
            print("1.Add Employee\n2.Remove Employee\n3.Show All Employees\n4.Exit Managing Pannel")
            ManagingAction=int(input())
            if ManagingAction==1:
                print("----- Enter Employee Information -----")
                username=input("Username ")
                password=input("Password ")
                name=input("Name ")
                family=input("Family ")
                email=input("Email ")
                result=self.addEmployee(username,password,name,family,email)      
                if result:
                  print("----- New Employee Added -----")
                else: 
                  print("----- New Employee Not Added due to Repitition or Being Invalid-----")
            elif ManagingAction==2:
                print("----- Enter Username to Remove -----")
                username=input("Username ")
                result=self.removeEmployee(username)
                if result :
                   print(f"----- Employee {username} Removed -----")
                else: 
                   print(f"----- Employee {username} Not Removed -----")
            elif ManagingAction==3:
                self.showEployees()
            elif ManagingAction==4:
                print("----- Exit Manager Pannel -----")  
                ManagerMode=False
            else:
                print("----- Invalide Managing Action -----")              
            
          

    #add new employee to list
    #first validation is checked
    #then repitition is checked 
    #finallt it is added to list
    def addEmployee(self,username,password,name,family,email):
         newEmployee=Employee(username,password,name,family,email)
         if (newEmployee.user is None) or (newEmployee.password is None) or (newEmployee.email is None):
            print("Information for Employee is Not Valid\nTry one more time !")
            return False 
         result=self.employeeRepitionCheck(newEmployee)
         if result:
            self.employees.append(newEmployee)
            return True
         else:
            return False
        

    #remove emoployee from list by its username
    #first existance of employee
    #then it is removed from list
    def removeEmployee(self,username):
        for e in self.employees:
            if e.user==username:
                idx=self.employees.index(e)
                self.employees.pop(idx)
                return True
        return False
    #show list of employees 
    def showEployees(self):
        if len(self.employees)==0:
            print("Employee List is Empty")
        else:
            idx=1
            for e in self.employees:
                print(f"{idx} : {e}")
                idx+=1
        return
    


    #check if newemployee 's username or email exists in the list or not
    def employeeRepitionCheck(self,newEmployee):
        if len(self.employees)==0:
            return True
        for emp in self.employees:
            if emp.user== newEmployee.user:
                print(f"Username {emp.user} Exists,choose different Username and try again!")
                return False
            if emp.email==newEmployee.email:
                print(f"E-mail {emp.email} Exists,choose different E-mail and try again!")
                return False
        return True  
      
    #return list of employees
    def getEmployees(self):
        return self.employees