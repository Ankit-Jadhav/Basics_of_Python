s1 = {1,2,3,4,3}
s2 = {4,5,6}
print(s1.union(s2))         #Union
print(s1, s2)
print(s1.intersection(s2))   #Intersection
#Update
s1.update(s2)     #S2 value updated in s1
print(s1,s2)

s6= {"a","b","c","d","a"}
s7= {"b","a","f"}
s6.intersection_update(s7)    #common values updated in s6
print("Intersection Update : ",s6)
 


s3 = {1,2,3,4,3}
s4 = {4,5,6}
s5= s3.update(s4)     #Wrong
print(s5)

s3.update(s4)
print(s3)         #S3 will be updated

#Symmetric Difference
#(A U B) - (A n B)

s8= {"a","b","c","d","a"}
s9= {"b","a","f"}
s10 = s8.symmetric_difference(s9)
print(s10)
print(s8)

s8.symmetric_difference_update(s9)   #update in s8
print(s8)


#difference() and difference_update()
s11= {"a","b","c","d","a"}
s12= {"b","a","f"}
s13= s11.difference(s12)      # Uncommon values of s11
print(s13)

s11.difference_update(s12)
print(s11)



#isdisjoint()
#The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
s14= {"a","b","c","d","a"}
s15= {"b","a","f"}
s16= {0,1,2}
print(s14.isdisjoint(s15))
print(s14.isdisjoint(s16))

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

s14= {"a","b","c","d","a"}
s15= {"b","a"}  
print(s14.issuperset(s15))
print(s15.issubset(s14))      #Subset


# add()
# If you want to add a single item to the set use the add() method.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


# update()
# If you want to add more than one item, simply create another set or any other iterable (list, tuple, dictionary), and use the update() method to add it into the existing set.
 
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Nagpur", "Pune"}
cities1.update(cities2)
print(cities1)

#Remove()/discard()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

#The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.


#pop() - pop()
# This method removes the last item of the set but the catch is that we don't know which item gets popped as sets are unordered.
# However, you can access the popped item if you assign the pop() method to a variable.

cities2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3= cities2.pop()
print(cities2)
print(cities3)


#del
# del is not a method, rather it is a keyword which deletes the set entirely.

cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities4
#print(cities4)

#clear(): clear all the items of set and print empty set
cities5 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5.clear()
print(cities5)

#Check if the item exists..
info = {"Carla", 19, False, 5.9}

if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")





