# Write Python code to insert an element in array.
import math


arr1 = [10,30,40,50]
element = 20
index = 2
arr1.insert(2, 20)
print(f" Que1 : Inserted updated array : {arr1}")


#2. Write Python code to remove duplicates from an array.
arr2 = [1,2,2,2,3,4,5,6,7,8,5,5,1]
unique_arr = []

def uniqueArray(arr):
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)

uniqueArray(arr2)
print(f"Que2: unique_array: {unique_arr}")

#3. Write a python program to reverse first and last digit of number without converting it into a string.
#number = int(input("Please enter a number"))

def reverse_first_last_digit(number):
    if number < 10:
        return number
    elif number <100:
        last_digit = number % 10
        first_digit = number // 10
        return ((last_digit*10) + first_digit)
    else:
        last_digit = number % 10      #remainder - %
        power = int(math.log10(number))
        print(power)
        first_digit = number // (10**power)            #floor division

        middle_digits = number % (10**power) 
        middle_digits = middle_digits // 10

        updated_digit = (last_digit * (10**power) ) + middle_digits* 10 + first_digit
        return updated_digit
    
    
# --- Input Handling with try-except ---

try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise ValueError("Please enter a positive integer.")
    elif number ==0:
        print ("0")
    else : 
        result = reverse_first_last_digit(number)
        print(result)
except ValueError as e:
    print (e)


    




