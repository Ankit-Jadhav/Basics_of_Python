import pytest
from functools import wraps

def log_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Loggin start of {func.__name__}")
        result = func(*args, **kwargs)
        print(f"loggin end of {func.__name__}")
        return result
    return wrapper

@log_func
def login(name,password):
    print(name, password)

login("Ankit","Test")


