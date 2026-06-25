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
if EntranceMode==1:
    manager.manage_panel()
elif EntranceMode==2:
    print("----- Enter as a Employee -----")    
elif EntranceMode==3:
    print("----- Enter as a Customer -----")   
elif EntranceMode==4:
    print("----- Bye -----")
else:
    print("----- Invalide Entrance Mode -----")    


