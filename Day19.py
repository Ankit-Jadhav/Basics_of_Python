#break statement
for i in range(12):
    print("5X", i+1, "=", 5*(i+1))
    if(i==9):
        break 
#break statement stops the loop

for u in range(15):
    if(u==10):
       break
    print("u: 5X", u+1, "=", 5*(u+1))    #for u==10 - loops stop

 #continue statement stops the iteration for specific condition

for w in range(15):
    if(w==10):
        continue
    print("w:5X",w,"=",5*w)
# for 10 the statement not worked and then continued



# do while loop
x = 0
while True:        #inifinte loop
    print(x)
    x = x+1
    if(x%100==0):
        break

#break statement
#The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.   

for i in range(1,101,1):
    print(i, end = " ")
    if(i==50):
        break
    else:print("Mississippi")
print("Thank You")
     

# Summary:

# Your code	Result
# print(i, end=" ")	prints number and stays on same line (space only)
# print(i)	prints number and moves to next line automatically

#Continue Statement: The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for i in [2,3,4,5,6,8,0]:
    if(i%2!=0):
        continue
    print(i)