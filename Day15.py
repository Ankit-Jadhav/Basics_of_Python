#Greeting Wish Excercise
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour= int(time.strftime('%H'))
print(hour)

timestamp = int(time.strftime('%M'))
print(timestamp)

timestamp = int(time.strftime('%S'))
print(timestamp)

if(12>hour>=5): 
    print("Good Morning")
elif(17>hour>=12):
    print("Good Afternoon")
elif(21>hour>=17): 
    print("Good Evenvinig")
else:
    print("Good Night")

