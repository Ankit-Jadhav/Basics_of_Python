# Que1 : Shift all zeroes or any other number to the end left or end right.
list1 = [1,2,3,0, 0,4464,1,2,4,5,7,-1,-2]
a = [x for x in list1 if x != 0 ]
b = [x for x in list1 if x ==0]
print(a + b)

#Que2 : Print list of all even and odd numbers
list1 = [1,2,3,0, 0,4464,1,2,4,5,7,-1,-2]

even_list = [x for x in list1 if x%2 ==0]
odd_list = [x for x in list1 if x%2 !=0]

print(even_list)
print(odd_list)

#Que3 : Rotate towards right from k element
list1 = [1,2,3,0, 0,4464,1,2,4,5,7,-1,-2]

index = list1.index(0)     # index of element from where we have to rotate right
print(index)
print(list1[index:] + list1[:index])

#Que4:Separate unique and duplicate list from main list
list1 = [1, 2, 3, 3, 5, 5, 6, 7]
unique_list = []
duplicate_list = []

for x in list1: 
    if x not in unique_list and x not in duplicate_list:
        unique_list.append(x)
    elif x in unique_list:
        unique_list.remove(x)
        duplicate_list.append(x)
print(unique_list)
print(duplicate_list)
    

#Que5: Remove any single element from the list
list1 = [1, 2, 3, 3, 5, 5, 6, 7]
list1.remove(2)
print(list1)


#Que6: Remove all duplicate element from the list
list1 = [1, 2, 3, 3, 5, 5, 6, 7]
list1 = [x for x in list1 if x !=3]
print(list1)

#Que7:Remove multiple duplicate elements from the list
list1 = [1, 2, 3, 3, 5, 5, 6, 7]

dup_list = [3,5]

list1 = [x for x in list1 if x not in dup_list]
print(list1)

#Que8: Use of pop() and remove()
list1 = [1, 2, 3, 3, 5, 5, 6, 7]
#remove the last element
list1.pop()
print(list1)

list2 = [1, 2, 3, 3, 5, 5, 6, 7,4,5,3]
list2.pop(4)    #index 4 pop
print(list2)

list3 = [1, 2, 3, 3, 5, 5, 6, 7,4,5,3]
list3.remove(3)   # remove the first occurence 3
print(list3)

#Que9: Print all unique element , duplicate element and duplicate element frequency

list3 = [1, 2, 3, 3, 5, 5, 6, 7,4,5,3]
unique_list = []
dup_list = []
dup_freq = {}

for x in list3:
    if x not in unique_list and x not in dup_list:
        unique_list.append(x)
    elif x in unique_list:
        unique_list.remove(x)
        dup_list.append(x)
        dup_freq[x] = 2 
    
    elif x in dup_list:
        dup_freq[x] += 1 

print(unique_list)
print(dup_list)
print(dup_freq)

#Que10: Use of count
list1 = [1, 2, 3, 3, 5, 5, 6, 7]
print(list1.count(3))

# frequency of all the element
from collections import Counter
list1 = [1, 2, 3, 3, 5, 5, 6, 7]
freq = Counter(list1)
print(freq)
print(freq[3])

#Que11: Replace the value in list with old value
list1 = [1,2,3,4]
list1[list1.index(2)] = 99
print(list1)

#Alertnate way
list1 = [1,2,3,4]
list1[1]=99
print(list1)

#Que12: Print the index of any input search

arr = [1, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9]
indices = []
search = 3
for i in range(len(arr)):
    if arr[i] == search:
        indices.append(i)
       
if indices:
    print(indices)

else:
        print("Element not found")


#Que13: Add value at specific position and shift other values to right
lst = [1, 2, 3, 4]
lst.insert(1, 100)
print(lst)

#Que14: Swapping of first and last digit
lst = [1, 2, 3, 4]
lst[0],lst[-1] = lst[-1], lst[0]
print(lst)

#Que15: Check list is palindrome or not
arr = [1,2,1]
print("Palindrome" if arr ==arr[::-1] else False)

#Que16: print key, value or full dict 
dict1 = {"name":"Ankit", "age":28, "Status" : True}
print(dict1)
print(dict1["name"])
print(dict1.items())
print(dict1.values())
print(dict1.keys())

#Que17: Add new key value pair in dict or update existing key value pair.
dict1 = {"name":"Ankit", "age":28, "Status" : True}
dict1["City"] = "Jaipur"   #Add a new key value pair

#Update - existing
dict1["age"] = 26
print(dict1)

#Que18: Get the index of an element in a list - use .index method
arr = [1, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9]
index = arr.index(3)
print(index)

#Que19: Second larget element of list. use of sorted, set..
list1 = [1, 2, 3, 4464, 1, 2, 4, 5, 7, -1, -2]
a = set(list1)
print(sorted(a))
print(sorted(a)[-2])

#Que20: Descending order, use of reverse in list
list1 = [1, 2, 3, 4464, 1, 2, 4, 5, 7, -1, -2]
print(sorted(list1, reverse = True))

#Que21: Use of SET

#SET
expected_roles = set(["admin", "user", "editor"])
actual_roles = set(["editor", "admin", "user", "user"])

if expected_roles == actual_roles:
    print("Test passed :Roles matched")
else:
    print("Test failed :Roles not matched")

#Que22: Use of FROZENSET
access_roles = {
    frozenset(["admin", "user"]) : "Full Access",
    frozenset(["user"]): "Limited Access"
}

test_roles = frozenset(["user", "admin"])

if test_roles in access_roles:
    access = access_roles[test_roles]
else:
    access = "No Access"

print(access)

#Que23: Use of PASS -- it will still print the value
students = ["Amit", "", "Ravi"]
for x in students:
    if x =="":
        pass   # Ignore blank name
    print(x)
#It still prints the blank name, because pass doesn’t skip anything — it’s just a placeholder.

#Que24: Use of CONTINUE --You call a name, realize it's invalid, and say "skip this one".
students = ["Amit", "", "Ravi"]
for s in students:
    if s == "":
        continue  # Skip printing blank name
    print("Calling:", s)

#Que25: Use of Break
students = ["Amit", "", "Ravi", "Pooja"]
for s in students:
    if s == "":
        print("Blank name found! Stopping...")
        break  # Immediately exit the loop
    print("Calling:", s)

#Que26: try and except method: 
#Case:1

try:
    x = 10/0
except ZeroDivisionError:
    print("Invalid")

#Case:2

def test_divison(a,b):
    try:
        result = a/b
        print(result)
    except ZeroDivisionError:
        print("Invalid")
    except TypeError:
        print("Error : Invalid input type")

test_divison(5,2)
test_divison(5,0)
test_divison(5,"2")

#Que26: Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

#Que27: 
