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


    
#Palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))


#Decorator
def my_decorator(func):
    def wrapper():
        print("something before the function")
        func()
        print("something after the function")
    return wrapper

@my_decorator
def say_something():
    print("Hello!")

say_something()



#ListDict
list = [1,2,43,True, "Ankit"]
print(list[4])

dict ={ 'name': 'Ankit', 'age': 26, 'Status':True}
print(dict['name'])

list.append(56)
print(list)
dict['Dob'] = '1996-10-30'
print(dict)


#ListTuple
my_list = [0, True, "Ankit"]
print(my_list[1])
print(my_list)

my_touple = (0, True, "Ankit")
print(my_touple[2])
print(my_touple)

for item in my_touple:
    print(item)

#Arithmetic Operator
def discount_calculator(price,discount):
    return price - (price*discount/100)

def test_10_percent_discount():
    assert discount_calculator(200, 10) ==180
def test_0_percent_discount():
    assert discount_calculator(200, 0) ==200
def test_0_percent_discount():
    assert discount_calculator(200, 100) == 0

#Asserstion
def assert_test():
    assert 5 + 5 == 11
assert_test()

#Attribute Error
def test_attribute_error():
    name = 'Ankit'
    print(name.push())
    # ❌ Strings have no 'push'
test_attribute_error()

#