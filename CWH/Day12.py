#Stirng Slicing
#for functions we use paranthesis
# for slicing we use square bracket
names =  "Harry,Ankit"
print(len(names))
fruit = "Mangoes"
print(fruit[3])
print(fruit[0:5])  #end index-1
print(fruit[:3])    # bydefault it pick starting index as 0
print(fruit[0:-3])    # byfeault it will pick in -ve case as -- len(fruit)-3  = 7-3 = 4 -- till g 
print(fruit[0:len(fruit)-3])   # same as above
print(fruit[-3:-2])    #7-3 : 4 means o and 7-2 : 5   e -- result o


