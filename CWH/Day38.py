#Custom Errors
a = int(input("Enter the value between 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")



#refer document of built in exceptions of python

##Defining Custom Exceptions-In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an API, etc.
#Here's the syntax to define custom exceptions:
'''class CustomError(Exception):
    # code ...
    pass

try:
    # code ...
    
except CustomError:
    # code...       
    # '''

user_input= input("Enter the value between 5 and 9: ")


if user_input.lower() =="quit":
    print("valid input")

else:
    try:
        b=int(user_input)
        if(9>=b>=5):
            print("valid input")
        else:
            raise ValueError("Value should be between 5 and 9")
    
    except ValueError:
        raise ValueError("Invalid input. Please enter a number between 5 and 9 or 'quit'.")

