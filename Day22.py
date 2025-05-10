 #Python Lists
marks= [3,5,6,"harry",True]
print(marks)
print(type(marks))
print(marks[2])
print(len(marks))

#Negative indexing
#length - index

print(marks[-3])     #negative index
print(marks[len(marks)-3])   #positive index
print(marks[2])
#above all three are same

#Check weather and item is present in the list or not....
if "harry" in marks:
    print("Yes")
else:
    print("No")

# for strings
if "arry" in "harry":
    print("yes")

#Slicing
print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:-1])
print(marks[1:4])
print(marks[1:4:2])

#if nothing in starting index --- python put 0 there
#if nothing in ending index --- python put length of index there
print(marks[:2])
print(marks[0:2])

print(marks[0:])
print(marks[0:5])


#List Comprehension

lst = [i for i in range(4)]
print(lst)

lst1 = [u*u for u in range(4)]
print(lst1)

lst2 = [w*w for w in range(10) if w%2==0]
print(lst2)