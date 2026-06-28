import re

BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
YELLOW = '\033[93m'


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
        return f"{GREEN}{self.user}       {self.password} {RESET}"

    #check validation
    #username and password must be str
    #check password with validate_password
    @staticmethod
    def checkValidation(username,password):
        
        if not(isinstance(username,str)) or not(isinstance(password,str)) :
           raise TypeError(f"{RED}Username and Password Must be String !{RESET} ")
         
        Applicant.validate_password(password)
        return True
    #check if passord contain alphabet,digit and special chars @,&
    @staticmethod
    def validate_password(password):
        pattern = r"^(?=.*[@&])(?=.*[0-9])(?=.*[a-zA-Z]).*$"
        if re.match(pattern, password):
           return True
        raise ValueError(f"{RED} Password must be combination of alphabet,digit and one of(@,&)!{RESET}")
        
   