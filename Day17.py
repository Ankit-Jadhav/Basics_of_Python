#For Loop
#Print every charachter
name1 = "Ankit Jadhav"
for i in name1: 
    print(i)


# every we get a in the name print gotachh
name2 = "aniket Singh Sahab"
for i in name2:
    print(i)
    if(i=="a"):
        print("gotachh")

'''Introduction to Loops:
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

for loop
while loop

The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
'''

#Example: iterating over a string:


name3 = 'Aniket'
for i in name3:
    print(i, end=", ")

print("\n")


#Example: iterating over a list:
Colours1 =["Red","Yellow","Blue","Pink"]
for x1 in Colours1:
    print(x1)
    for letter1 in x1:    #print every letter also in colours
        print(letter1)

#Example: iterating over a list:
Colours2 =["Red","Yellow","Blue","Pink"]
for x2 in Colours2:
    print(x2)

print()   
    
for x2 in Colours2:    #print every letter also in colours
    for letter2 in x2:
        print(letter2)
    print()

#Range
#Argument -- value in paranthesis of range(argument1,argument2,argumente3)
'''range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.'''

#print k start from 0 to 4
for k in range(5):
    print(k)

print()

#print k from 1 to 5
for k in range(5):
    print(k+1)

print()

#print k from 2 to 6
for k in range(5):
    print(k+2)

#range(starting_index,ending_index-1,steps)
# range(5) -- bydefault start is 0 
print()

for k in range(5, 10):
    print(k)

print()
for k in range(1,14,3):
    print(k)

#Explore about third parameter of range (ie range(x, y, z))
 


