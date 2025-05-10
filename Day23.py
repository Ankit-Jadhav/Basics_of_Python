#List Methods
l = [11,45,1,2,4,6]
print(l)
l.append(7)    # method of list - put 7 at the end
print(l)

m = [11,45,1,2,4,6]
m.sort()       #method of list - put values in ascending order
print(m)

o = [11,45,1,2,4,6]
o.sort(reverse=True)    # in descending order
print(o)

p =[11,45,1,2,4,6]
p.reverse()       #reverse the order
print(p)

q = [11,45,1,2,4,6,1]
print(q.index(1))        #give index of 1 -- first occurence

print(q.count(1))       # count of 1

r = q.copy()
r[0] = 0
print(r)
print(q)

#insert - replace
r.insert(1,899)
print(r)

#extend
s= [100,200,300]
q.extend(s)
print(q)

#Concateating
s= [100,200,300]
t= [400,500,600]

u = s + t
print(u)

print(len(u))

#index count
indexCounting= len(u) - 1
print(indexCounting)
