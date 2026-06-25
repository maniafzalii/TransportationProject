import re

class Applicant:
    def __init__(self,user:str,password:str):
        result=Applicant.checkValidation(user,password)
        if result:
            self.user=user
            self.password=password
            print("Applicant Created")
        else:
            self.user=None
            self.password=None   

    #check 2 applicant equality on their username
    def __eq__(self, other):
        if not isinstance(other,Applicant):
            print("Input Argument is not Applicant instance")
            return False
        if self.user is None or other.user is None:
            return False
       
        if self.user!=other.user:
            return False
        return True
                
    def __repr__(self):
        return f"username {self.user} , password {self.password}"

    #check validation
    #username and password must be str
    #check password with validate_password
    @staticmethod
    def checkValidation(username,password):
        
        if not(isinstance(username,str)) or not(isinstance(password,str)) :
           print("Username and Password must be String !") 
           return False
        
        result=Applicant.validate_password(password)
        if result:
            return True
        else:
            print("Password must be combination of alphabet, digits and one of (@,&)!") 
            return False  
    #check if passord contain alphabet,digit and special chars @,&
    @staticmethod
    def validate_password(password):
        pattern = r"^(?=.*[@&])(?=.*[0-9])(?=.*[a-zA-Z]).*$"
        if re.match(pattern, password):
           return True

        else:
           print("Not Valid password , try again !!")
           return False
        
    #check if email follows defines structure    
    @staticmethod
    def validate_email(email):
        pattern = r".+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
           return True
        else:
           print("not valid email ! try again")
           return False


            
    