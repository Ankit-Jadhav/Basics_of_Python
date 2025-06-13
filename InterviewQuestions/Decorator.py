def my_decorator(func):
    def wrapper():
        print("something before the function")
        func()
        print("something after the function")
    return wrapper

@my_decorator
def say_something():
    print("Hello!")

say_something()