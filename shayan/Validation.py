import re


def validate_password(password):
    pattern = r"^(?=.*[@&])(?=.*[0-9])(?=.*[a-zA-Z])[a-zA-Z0-9@&]*$"
    if re.match(pattern, password):
        print("Valid Password")
    else:
        print("Not Valid password , try again !!")


def validate_email(email):
    pattern = r".+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        print("email saved")
    else:
        print("not valid email ! try again")



