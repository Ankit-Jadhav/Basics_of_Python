#Enumerate Function
marks= [12,40,50,60,70,89,1,32]

index = 0
for i in marks:
    print(i)
    if (index ==5):
        print("Very good")
    
    index +=1


#Using enumerate
for index, i in enumerate(marks,start=1):
    print(i)
    if(index ==5):
        print("Very good")

 
'''Enumerate function in python

The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

0 apple  
1 banana  
2 mango
 
 As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.'''

