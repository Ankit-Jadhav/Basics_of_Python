#Recursion- In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

#factorial(6)=6*5*4*3*2*1
#factorial(5)=5*4*3*2*1
#factorial(4)=4*3*2*1
#factorial(3)=3*2*1
#factorial(2)=2*1
#factorial(1)=1
#factorial(0)=1

#factorial(n)= n*facorial(n-1)
 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))

#Solution : 
#4*factorial(3)
#4*3*factorial(2)
#4*3*2*factorial(1)
#4*3*2*1


#fibonacci sequence
# f0 = 0
# f1 = 1
# f2 = f1 + f0
# fn = f(n-1) + f(n-2)


#0 1 1 2 3 5 8 ......
def fibonacci(m):
    if(m==0):
        return 0
    elif(m==1):
        return 1
    else:
        return  fibonacci(m-1) + fibonacci(m-2)

print (str(fibonacci(6)) + "\n")

#Print the series
for i in range(7):
    print(fibonacci(i))





