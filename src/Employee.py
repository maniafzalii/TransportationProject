from Applicant import Applicant

#subclass of applicant it has name,family and email as its own attributes
class Employee(Applicant):
    def __init__(self,user,password,name,family,email):
        super().__init__(user, password)
        self.name=name
        self.family=family
        validate_result=Applicant.validate_email(email)
        if validate_result:
           self.email=email
        else:
           self.email=None

    def __eq__(self, other):
        if not(isinstance(other,Employee)):
            print("Input Argument is not Employee instance")
            return False
        if self.email is None or other.email is None:
            return False
        if self.email!=other.email:
            return False
        return super().__eq__(other)

    def __repr__(self):
        return super().__repr__()+f" name {self.name} ,family {self.family} ,email {self.email}"    
   