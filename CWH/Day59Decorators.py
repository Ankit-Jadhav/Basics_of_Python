#Decorators
'''✅ Decorators in Python
A decorator in Python is a function that modifies the behavior of another function or method — without changing its source code. It's a powerful feature for reusable, clean, and DRY code.'''

# Decorator that logs before and after a function runs
def log_action(func):                          # A decorator function that takes another function (func) as an argument.
    def wrapper(*args, **kwrgs):     #This inner function wraps the original function. It can accept any number of positional and keyword arguments using *args and **kwargs.
        print(f"Executing : {func.__name__}")         #print(f" Executing: {func.__name__}") logs the function name before it runs.
        result = func(*args, **kwrgs)                     #calls the original function with the provided arguments.
        print(f"Completed: {func.__name__}")                #print(f" Completed: {func.__name__}") logs completion after it runs.
        return result                           #return result ensures that the original function's result is returned unchanged.
    return wrapper                               #Finally, log_action() returns the wrapper, replacing the original function with the decorated one.


@log_action
def add(a,b):
    return a+b

@log_action
def greet(name):
    print(f"Hello {name}!")


# ▶️ Test the decorated functions
result = add(5,3)
print(f"Result of add: {result}\n")

greet("Ankit")
