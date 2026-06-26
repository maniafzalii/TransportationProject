from Applicant import Applicant

#subclass of applicant it has name,family and email as its own attributes
class Employee(Applicant):
    def __init__(self,user,password,name,family,email):
        super().__init__(user, password)
        if not(isinstance(name,str)) or not(isinstance(family,str)):
            raise TypeError("Name and Family must be String")
        if not name.strip() or not family.strip():
            raise ValueError("Name and family can not be Empty!")
        Applicant.validate_email(email)
        self.name=name
        self.family=family
        self.email=email
        
    def __eq__(self, other):
        if not(isinstance(other,Employee)):
            return NotImplemented
        return self.user==other.user and self.email==other.email

    def __repr__(self):
        return super().__repr__()+f" , name {self.name} ,family {self.family} ,email {self.email}"    
   