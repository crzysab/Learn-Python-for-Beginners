#Add an element in Dict
MyDict = {1:'one', 2:'two', 3:'three'}
print("Before : ", MyDict)
MyDict[4] = "four"
print("After  : ", MyDict)

#Make new dict from keys and value
keys = {'a','i','u','e','o'}
value = 'vowel'
newDict = dict.fromkeys(keys,value)
print("New Dict : ",newDict)

#Access an element using key
MyDict2 = {"name":"sabrina","course":"python"}
print("My Dict 2 : ", MyDict2)
print("Name : ", MyDict2.get("name"))

#Access all element using 'items'
MyDict3 = {"name":"sabrina","course":"python"}
print("My Dict 3 : ", MyDict3.items())

#Update value in Dict
MyDict4 = {1:'one', 2:'four', 3:'three'}
print("Before : ", MyDict4)
up = {2:'two'}
MyDict4.update(up)
print("After  : ",MyDict4)

#Delete an element in dict
MyDict5 = {1:'one', 2:'two', 3:'three'}
print("Before : ", MyDict5)
MyDict5.pop(2)
print("After  : ",MyDict5)

#Check a key in dict
MyDict6 = {1:'one', 2:'two', 3:'three'}
print("1 in MyDict6 : ", 1 in MyDict6)

#Lenght of Dict
MyDict7 = {1:'one', 2:'two', 3:'three'}
print("Lenght of MyDict7 : ", len(MyDict7))