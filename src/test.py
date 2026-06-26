from Applicant import Applicant
from Employee import Employee
from Manager import Manager

print("----- Welcome to Transportaion Pannel -----")
print("----- Define Manager Username and Password -----")
print("----- Be Carefull Username and Password can be contain alphabet,numbers,@,& -----")

managerDefine=True
username=input("Username ")
password=input("Password ")
manager=Manager(username,password)
while managerDefine:
    if(manager.user is None)or( manager.password is None):
       print("Re Enter Username and Password")
       username=input("Username ")
       password=input("Password ")
       manager=Manager(username,password)
    else:
        managerDefine=False
print("----- Manager Defined Successfully -----") 
print("----- Choose Your Role in the Pannel -----")
print("1.Manager\n2.Employee\n3.Customer\n4.Exit Pannel")
EntranceMode=int(input())
run=True
while run:
    if EntranceMode==1: 
        managerVelidated=False
        while not(managerVelidated):
            print("----- Enter Username and Password to Enter as Manager -----")
            username=input("Username ")
            password=input("Password ")
            result=manager.validate_entrance(username,password)
            if result:
               managerVelidated=True
            else:
               print("----- Your Entrance data Not Correct -----")
               print("----- Whta is your next Action? -----")
               print("1.Enter Entrance Data\n2.Exit Current Menu")
               mode=int(input())
               if mode==1:
                  continue
               else:
                  break
        if managerVelidated:
           manager.manage_panel()
                  
    elif EntranceMode==2:
       print("----- Enter as a Employee -----")    
    elif EntranceMode==3:
       print("----- Enter as a Customer -----")   
    elif EntranceMode==4:
       print("----- Bye -----")
       run=False
    else:
       print("----- Invalide Entrance Mode -----")    
    EntranceMode=int(input())

