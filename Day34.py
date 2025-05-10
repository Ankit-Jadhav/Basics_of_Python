#Dictionary Methods
ep1= {120: 60, 125: 70, 130: 75, 140: 80}
ep2 = {145: 56, 150: 78}
#Update
ep1.update(ep2)     #update ep1
print(ep1)
print(ep1.clear())    #empty dict

#print empty dict
ep3= {}
print(ep3)
#pop -- to remove any item
ep4 = {120: 60, 125: 70, 130: 75, 140: 80}
print(ep4.pop(120))
print(ep4)

#popitem removes the last value
ep4.popitem()
print(ep4)

#del
del ep4   # it will delete ep4 and gives error
# print(ep4)  
ep5 = {120: 60, 125: 70, 130: 75, 140: 80}
del ep5[120]
print(ep5)

    