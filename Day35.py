#Else loop in python 
#else can also be use directly with for , while loop. 

for i in range(5):
    print(i)
else:
    print("Loop over")


for u in range(6):
    print(u)
    if(u ==4):
        break
else:
    print("Loop over")


#While loop
i = 0
while i<7:
    print(i)
    i = i + 1
else:
    print("Loop over")


# The .format() method in Python is used to insert values into a string at specific placeholders marked by {}.

for x in range(5):
    print("iteration no {} in for loop".format(x + 1))
else:
    print("else block in loop")
print("Out of loop")

