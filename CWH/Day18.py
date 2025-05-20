#While loop
i = int(input("Enter the value of i : "))
while(i<10):
    print(i)
    i = i +1

print(i)

# print till invalid data
u = int(input("Enter the value of u: "))
while(u<=15):
    u = int(input("Enter the value of u: "))
    print(u)

#Decrementing Loop
count = 10
while(count>6):
    print(count)
    count = count - 1

 #Else with while loop

count1 = 8
while(count1 >5):
    print(count1)
    count1 = count1 - 1
else: 
    print(" I am inside else")


#do while loop not exist in do while loop..check js for this


'''Python while Loop
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.
Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.'''

#Do-While loop in python
'''do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.
How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:'''
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break 
  