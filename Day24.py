#Tuples
#Immutable
tup=(1,2,3,4,5, "green", True)
print(type(tup), tup)
# tup[0] = 90 -- Will give error -- unchangeable

tup1=(1,)
print(type(tup1), tup1)    #this is considered as type tuple

tup2=(1)
print(type(tup2), tup2)   #this is considered as type int

print(tup[0])   # Value at 0 index
print(len(tup))
print(tup[-1])    #len-1


#check if value is present or not
if False in tup:
    print("Not present")

#Range of Index:
# Tuple(start:end:jumpIndex)
print(tup[1:4])