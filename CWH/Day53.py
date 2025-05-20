
#use of for loop to print cube of array
arr1 = [1,2,3,4,5,6]
cube_arr1 = []

def cubeArr(arr):
    for i in arr:
     cube_arr1.append(i**3)

cubeArr(arr1)
print(cube_arr1)
arr2 = arr1 +cube_arr1
print(arr2)
 


#map
#map(function,iterable)
#Map, Filter, Reduce
def cube(x):
   return x**3
print(cube(2))

#using map and lambda function print cube of every element of an array
arr3 = [1,2,3,4,5,6,7,8,9]

cub_arr3 = list(map(lambda x: x**3, arr3))
print(f"cube_arr3: {cub_arr3}")


#using list comprehension
arr4 =[1,2,3,4,5,6,7,8,9]
cub_arr4 = [x**3 for x in arr4]
print(f"list comprehension:{cub_arr4}")


#Using while loop
arr5 =[1,2,3,4,5,6,7,8,9]
cub_arr5= []

i = 0
while i < len(arr5):
   cub_arr5.append(arr5[i]**3)
   i+=1
print(f"While loop : {cub_arr5}")

#Filter
#use of filter to give answer for particular condition
arr6 =[1,2,3,4,5,6,7,8,9]

filter_function = filter(lambda x: x>3, arr6)
map_function = map(lambda x:x**3,filter_function)
result = list (map_function)
print(result)



#use of list comprehension
arr7 =[1,2,3,4,5,6,7,8,9]
listComp = [x**3 for x in arr7 if x >5]
print(listComp)


#use of reduce
from functools import reduce

arr8 = [1,2,3,4,5,6,7,8,9]

def sumXY(x,y):
   return x+y

sum1 =reduce(sumXY, arr8)
print(sum1)

sum2 = reduce(lambda x,y : x+y, arr8)
print(sum2)


#find the maximum value in the list
arr8 = [1,2,34,6,70,888,56,3,4,5,6,7,8,9]
max_value = reduce(lambda x,y:x if x>y else y, arr8)
print(max_value)


