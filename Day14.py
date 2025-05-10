#If Else Statement
# a = int(input("Enter your age "))      #typecasting because input value stores in string format
# print("Your age is :", a)  

# Conditional Operators
#  > < == >=  <=  !=
# print(a>18)
# print(a<18)
# print(a==18)
# print(a>=18)
# print(a<=18)
# print(a!=18)


# #IF ELSE
# if(a>18): 
#     print("Eligible")      #space given -- indentation -- inside if block --
# else: 
#     print("Non-eligible")   #these two are different
# print("Elgible")     #out of if else statement


#ELSE IF
# if apple price is less than 50 rs by 2 kg , if less than equal to  25 by 4 kg , if greater than 50 by 1 kg . if greater than 70 by half kg. 
a = int(input("Please enter apple price: "))
if (100>a>70): 
    print("buy 0.5 kg" )
elif(70>a>50):
    print("buy 1 kg")
elif(50>a>25):
    print("buy 2 kg")
elif(0<a<=25):
    print("buy 4 kg")
else:
    print("no buy")

#nested if statements
b = int(input("Please enter banana price: "))
if(b>50):
    if(70>b>50): 
        print("1kg")
    else:
        print("0.5kg")
elif(0<b<50):
    if(b<20):
        print("buy 2 kg")
    else:
        print("buy 4 kg")
else: 
    print("no buy")

    


