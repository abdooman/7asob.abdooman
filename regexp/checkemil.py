import re

email = input('pleas enter your email: ')
def isEmail():
    is_email = re.search(r'^[A-z0-9]+[\.-]?[A-z09]+@\w+\.\w{2,3}$', email)

    if is_email:
        print(f'the {email} is a valid Email')

    else:
        print('is not a valid Email')

if(email):
    isEmail()