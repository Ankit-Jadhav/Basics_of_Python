lr =int(input("enter the lower range"))
ur= int(input("enter the upper range"))

prime_list = []
if(ur>lr and lr>1):
    for num in range(lr, ur+1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            prime_list.append(num)
        
print(prime_list)