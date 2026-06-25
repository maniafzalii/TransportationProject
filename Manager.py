from Applicant import Applicant
class Manager(Applicant):
    def __init__(self, user, password):
        super().__init__(user, password)