# #Finally keyword- Finally Clause
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

'''try:
    # statements which could generate exception
except:
    # solution of generated exception
finally:
    # block of code which is going to execute in any situation'''


#The finally block is executed irrespective of the outcome of try......except......else blocks.
#One of the important use cases of finally block is in a function which returns a value.


"Question: Why dont we use print statement directly instead of finally keyword?"

try:
    l=[1,2,3,4]
    i = int(input("Enter the index value: "))
    print(l[i])

except:
    print("Invalid input value")

finally: 
        print("Finally statement")

#print("Print statement directly in place of finally keyword")


"Question: Why dont we use print statement directly instead of finally keyword?"
#Answer: Under the function with return statement the normal print statement will not work but finally keyword works..


def func1():
     try:
          l = [1,2,3,4,5]
          i= int(input("Enter the index value"))
          print(l[i])
          return 1
     except:
          return 0
     
     finally:
          print("Finally statement")
          
          #print("Print statement")
        
x = func1()
print(x)

          



    


