#Manipulating tuples
#it is immutable - for manipulation first convert tuples to list and then perform the required options and convert it back to tuple.
tup= (1,2,3,4,5,6)

tup1 = list(tup)
tup1.append(9)
print(tup1)
tup1.pop(3)     #remove item of mentioned index
print(tup1)
tup1[4]=50     #change item
print(tup1)
tup5=tuple(tup1)
print(tup5)


#concate can be done directly
tup2= ("a","b","c")
tup3= ("d","e","f")
tup4 = tup2+tup3
print(tup4)

#Tuple Methods
#count ---- count of repeat values
tup6=(4,4,4,4,4,6,7,4)
print(tup6.count(4))

#Index -- first occurence of value
print(tup6.index(4))

#index.(element,start,end) --- find first occurence of element between start and end-1 value
#length of tuple
print(len(tup6))

