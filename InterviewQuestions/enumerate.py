#  What is enumerate() in Python?
'''enumerate() is a built-in Python function used when you need both the index and the value while looping over an iterable (like a list or string).

enumerate(iterable, start=0)

iterable: any iterable (like list, string, tuple, etc.)
start: the starting index (default is 0) '''

list1 = [1,2,3,4,5,5,1,4,5,7,8]

for index, value in enumerate(list1):
    print(index , value)

print("\n")
str1 = "Ankit Jadhav"

for index,value in enumerate(str1):
    print(index,value)


#Without enumerate

for i in range(len(list1)):
    print(i , list1[i])


# Calculate the frequency of char or value
