from src.Applicant import Applicant



BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
YELLOW = '\033[93m'

#subclass of applicant it has name,family and email as its own attributes
class Employee(Applicant):
    def __init__(self,user,password,name,family,email):
        super().__init__(user, password)
        if not(isinstance(name,str)) or not(isinstance(family,str)):
            raise TypeError(f"{RED}Name and Family must be String !{RESET}")
        if not name.strip() or not family.strip():
            raise ValueError(f"{RED} Name and family can not be Empty !{RESET}")
        Employee.validate_email(email)
        self.name=name
        self.family=family
        self.email=email
        
    def __eq__(self, other):
        if not(isinstance(other,Employee)):
            return NotImplemented
        return self.user==other.user and self.email==other.email

    def __repr__(self):
        return super().__repr__()+f"{GREEN} , name {self.name} ,family {self.family} ,email {self.email} {RESET}"    
    
     #check if email follows defines structure    
    @staticmethod
    def validate_email(email):
        if not(isinstance(email,str)):
            raise TypeError(f"{RED} Email must be String ! {RESET}")
        pattern = r"^[^@\s]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
           return True
        raise ValueError(f"{REDE} Email must follow format like: <<shiva@gmail.com>> {RESET}")

            
    