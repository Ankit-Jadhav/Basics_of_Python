def zero_division_error_fix():
    try: 
        result = 100/0 
    except ZeroDivisionError:
        print("Can't divide by zero")
zero_division_error_fix()



# def zero_division_error():
#     result = 100/0 
# zero_division_error()
