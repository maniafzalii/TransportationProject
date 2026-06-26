import re

class Applicant:

    def __init__(self,user:str,password:str):
    
        Applicant.checkValidation(user,password)
        self.user=user
        self.password=password

    #check 2 applicant equality on their username
    def __eq__(self, other):
        if not isinstance(other,Applicant):
           return NotImplemented
        return self.user==other.user
        
                
    def __repr__(self):
        return f"username {self.user} , password {'*'* len(self.password)}"

    #check validation
    #username and password must be str
    #check password with validate_password
    @staticmethod
    def checkValidation(username,password):
        
        if not(isinstance(username,str)) or not(isinstance(password,str)) :
           raise TypeError("Username and Password Must be String ")
         
        Applicant.validate_password(password)
        return True
    #check if passord contain alphabet,digit and special chars @,&
    @staticmethod
    def validate_password(password):
        pattern = r"^(?=.*[@&])(?=.*[0-9])(?=.*[a-zA-Z]).*$"
        if re.match(pattern, password):
           return True
        raise ValueError("Password must be combination of alphabet,digit and one of(@,&)!")
        
    #check if email follows defines structure    
    @staticmethod
    def validate_email(email):
        if not(isinstance(email,str)):
            raise TypeError("Email must be String")
        pattern = r"^[^@\s]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
           return True
        raise ValueError("Email must follow format like: <<shiva@gmail.com>> ")

            
    