def login_function_call(func):
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs = {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@login_function_call
def add(x,y,z,a):
    return x+y+z+a
print(add(3,4,5,a=6))
        