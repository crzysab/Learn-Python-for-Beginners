#Add 1 element in the end of List
list1 = ["Big Data","IOT","ML"]
print("List 1")
print("Before : ", list1)
list1.append("Python")
print("After  : ", list1)

#Add some element in the of list
list2 = ['a','b','c']
print("List 2")
print("Before : ", list2)
list2.extend(['d','e','f'])
print("After  : ", list2)

#Remove element from list
list3 = [1,2,3,4,5]
print("List 3")
print("Before : ", list3)
list3.remove(3)
print("After  : ", list3)

#Clear all element in list
list4 = [1,2,3,4,5]
print("List 4")
print("Before : ", list4)
list4.clear()
print("After  : ", list4)

#Remove element with pop
list5 = ['a','b','c','d']
print("List 5")
print(list5)
de = list5.pop(2) #To print removed element
print(de)

#Check index number
list6 = ['a','b','c','d','e']
print("List 6")
print(list6)
ind = list6.index('c')
print("Index number of C : ",ind)

#Count element in list
list7 = ['a','a','a','d','e']
print("List 7")
print(list7)
cou = list7.count('a')
print("element 'a' in list 7 : ", cou)

#Sort element by alpha
list8 = ["BigData", "ABC", "Python", "C#"]
print("List 8")
print("Before : ", list8)
list8.sort()
print("After  : ", list8)

#Reverse element in list
list9 = [3,5,1,0]
print("List 9")
print("Before : ",list9)
list9.reverse()
print("After  : ", list9)

#Copy element in list
list10 = [1,2,3,4]
print("List 10")
print("List 10      : ",list10)
print("List 10-Copy : ",list10.copy())

#Python Enumerate method in list
list11 = ['data','science','python','R']
print("List 11")
print("Before : ", list11)
data = enumerate(list11) #from 0 (default)
data2= enumerate(list11, 100) #from 100
print("After  : ", list(data))
print("After 2: ", list(data2))