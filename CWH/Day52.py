'''🔹 What is a Lambda Function in Python?
A lambda function in Python is a small anonymous function — meaning it doesn't have a name.

You use lambda when you need a quick function for a short period and don’t want to define a full function using def.

lambda arguments: expression

lambda → the keyword

arguments → like function parameters

expression → a single expression that gets returned

'''


#Normal Function : 
def fun(x,y):
    return x+y

print(fun(2,3))


#Lamba Function:
add = lambda x, y : x+y
print(add(2,3))

cube = lambda z: z*z*z
print(cube(3))


