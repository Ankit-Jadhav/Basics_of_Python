list1 = [1,2,3,4,5,6]
list2 = [6,1,3,5,6]
list1 = list1 + list2
print(list1)

list3 = ["a",1,3,4]
list4 = ["d",5,6,3]
list3.extend(list4)
print(list3)


list5 = []
list6 = []

for i in range(5):
    ele = int(input("enter element"))
    list5.append(ele)

for i in range(5):
    ele = int(input("enter element"))
    list6.append(ele)
    
list5 = list5 + list6
print(list5)