#Local vs Global Variable
x = 4    #global variable
print(x)

def hello():
    x=5
    y=1
    print(x)
    print(f"the value of local variable{x}")    #local variable



hello()
print(f"the value of global variable {x}")
# print(y) -- error - local variable


# i want to print local a outside
a = 10

def my_function():
    global a
    a  = 11


my_function()
print(a)


 
