MyNumList = [1,2,3,4,5,6,7,8] #Number List
MyStrList = ['python','java','C','C++'] #Str List
MyNumStrList = [1,'C#',3.14,6,'R'] #Mix List
My_list = ["Sabrina",[1,2,3],['a','b']] #List in List

Dup = MyNumList*2 #Duplicate list
print(Dup)

Con = MyStrList + MyNumList #Combine 2 list
print(Con)

#Accessing element from list
#indexing
print("My first number in MyNumList : ", MyNumList[0]) #Left Side
print("My last number in MyNumList : ", MyNumList[-1]) #Right Side

#Slicing
print("My second and third number in MyNumList : ", MyNumList[1:3])

#Check element on list
result = 3 in MyNumList
print(result)