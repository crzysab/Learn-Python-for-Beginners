#For Loop
MySet = {1,2,3,4,5}
for item in MySet :
    print("Line -", item)

#Add element using 'add'
MySet2 = {1,2,1,2,3}
print("Before : ", MySet2)
MySet2.add(4)
print("After  : ", MySet2)

#Add element using 'update'
MySet3 = {'big','data'}
print("Before : ", MySet3)
MySet3.update({'science'})
print("After  : ", MySet3)

#Remove first element in set
MySet4 = {0,1,2,3,4}
print("Before : ", MySet4)
MySet4.pop()
print("After  : ", MySet4)

#Remove an element using 'remove' in set
MySet5 = {0,1,2,3,4}
print("Before : ", MySet5)
MySet5.remove(3)
print("After  : ", MySet5)

#Remove an element using index number in set
MySet6 = {0,1,2,3,4}
print("Before : ", MySet6)
MySet6.discard(3)
print("After  : ", MySet6)

#Remove all element in set
MySet7 = {0,1,2,3,4}
print("Before : ", MySet7)
MySet7.clear()
print("After  : ", MySet7)

#Operation
a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}
c = {1,2}
d = {5,6}
print("a : ",a)
print("b : ",b)
print("c : ",c)
print("d : ",d)
print("a intersection b : ",a.intersection(b))
print("a union b : ",a.union(b))
print("a diference b : ",a.difference(b))
print("b diference a : ",b.difference(a))
print("a symmetric difference b : ", a.symmetric_difference(b))
print("c issubset a : ",c.issubset(a))
print("a issuperset c :",a.issuperset(c))
print("a isdisjoint d : ",a.isdisjoint(d))

#Set and Frozenset
A = {1,2,3}
print("A : ", A)
print("Type A : ", type(A))
B = frozenset({1,2,3})
print("B : ",B)
print("Type B : ", type(B))