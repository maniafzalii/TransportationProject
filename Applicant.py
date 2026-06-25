class Applicant:
    def __init__(self,user:str,password:str):
        result=self.validate(user,password)
        if result:
            self.user=user
            self.password=password
        else:
            self.user=None
            self.password=None    

    def __eq__(self, other):
        
        if (self.user==None)or  (other.user==None) :
            print("Your input is None")
            return False
        
        if len(self.user)!=len(other.user) :
            return False
        
        resultUser=True
        suser=list(self.user)
        ouser=list(other.user)
        for u in suser:
            idx=suser.index(u)
            if u!=ouser[idx]:
                resultUser=False
                break
               
        if resultUser:  
            return True     
        else:
            return False
                


            

    def validate(self,username,password):
          specialChar=['@','&']
          userCorrectionFlag=True
          passCorrectionFlag=True
          formatCorrectionFlag=True
          if (isinstance(username,str)) and (isinstance(password,str)):
          
            for s in str(username):
                if not(s.isalpha()) and not(s.isdigit()) and s!=specialChar[0] and s!=specialChar[1]:
                    userCorrectionFlag=False
                    break
            if userCorrectionFlag:
                for p in str(password):
                    if not(p.isalpha()) and not(p.isdigit()) and p!=specialChar[0] and p!=specialChar[1]:
                       passCorrectionFlag=False
                       break
                     
          else:
              formatCorrectionFlag=False
          if formatCorrectionFlag :
              if userCorrectionFlag and passCorrectionFlag:
                  return True
              elif userCorrectionFlag and not(passCorrectionFlag):
                  print("Password must be alphabet,digit,@,&")
                  return False
              elif not(userCorrectionFlag) and passCorrectionFlag:
                  print("Username must be alphabet,digit,@,&")  
                  return False
              else:
                   print("Username and Password must be alphabet,digit,@,&")
                   return False
          else:
              print("Username and Password must be String ")    
              return False
 
             
            
            
    