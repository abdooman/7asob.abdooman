class TooOldError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Sorry, you are too old."
class TooYongeError(Exception):
    def __init__(self):
        pass  
    def __str__(self):
        return "Sorry, you are too yonge."

def checkage(age):
    try:
        if age < 18:
            raise TooYongeError
        elif age > 50:
            raise TooOldError
    
    except TooYongeError as Error : 
        print(Error)
    except TooOldError as Error:
        print(Error)
    else:
        print("Welcome to the programing") 

print(checkage(int(input("Please Enter Your Age: "))))

