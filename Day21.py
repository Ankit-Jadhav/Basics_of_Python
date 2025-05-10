#Function Argument

#Default Argument

def average(a,b):
    print("The average of ", (a+b)/2)

average(4,6)

def average(c=5,d=8):
    print("The average of ", (c+d)/2)

average(9)      #default c = 9, d =8
average(d=10)

def name(fname,mname = "John", lname="watson"):
    print("Hello", fname,mname,lname)

name("Ankit",lname="Test")

#Keyword Arguments
# no order matter in this syntax
name(fname= "Ankit", lname="Test", mname="Aniket")


#Required Arguments 
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill") --- it is mandatory to pass lname as not assigned earlier

#when number of arguments passed matches to the actual function definition.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")


#Variable-length arguments:
#Arbitrary Arguments:

def Numbers(*numbers):
    print("Hello", name[0],name[1],name[2])

name(1,2,3)


def average(*digits):
    print(type(digits))                  # average is call tuple here
    sum = 0 
    for i in digits:
        sum = sum + i 
    
    print("Average is :", sum/ len(digits))

average(5,6,7)

def name(**name):
    print(type(name))            #name is in dictioney here 
    print("Hello, ", name["fname"], name["mname"],name["lname"])

name(mname = "Ankit", lname= "Aniket", fname = "James")  
 

#return statement
def Val(*values):
                    # average is call tuple here
    sum = 0 
    for i in values:
        sum = sum + i 
    return sum/len(values)      

c= Val(5,6,7,1)
print( c)
 
#check indentation for above program and for return statements

   
