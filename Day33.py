#Dictornaries
dic = {
    "Name": "Harry",
    "Age" : 28,
    "City": "Pune",
    "Status": False 
}
print(dic)
print(dic["Name"])
print(dic.get("Name"))

#In Python, a dictionary is a built-in data type that stores key-value pairs. Each key in a dictionary is unique, and it is used to access its associated value.
#Definition:
# A dictionary in Python is an unordered(ordered from python 3.7 version), mutable, and indexed collection of data values, where each value is accessed using a key instead of an index.

#if key does not exist and we want error in that print statement we use print(dic["Name"]). 
#if key does not exist and we do want error in that print statementt we use print(dic.get("Name"))..

# print(dic["Name1"])   #Will give error
print(dic.get("Name1"))

#to print all keys
print(dic.keys())
#to print all values
print(dic.values())

#to print all values
for i in dic.keys():
    print(dic[i])


#using f string

for key in dic.keys():
    print(f"The value corresponding to {key} is {dic[key]}")  


#key value pair
print(dic.items())

for key,value in dic.items():
    print(f"The value corresponding to {key} is {dic[key]}") 
