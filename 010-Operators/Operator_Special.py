#Membership operator
x = 'Hello World'
print("'H' in x : ", 'H' in x) #Return True
print("'S' in x : ", 'S' in x) #Return False
print("'T' not in x : ", 'T' not in x) #Return True

y = {1:'a', 2:'b'}
print("1 in y : ", 1 in y)
print("'a' in y : ", 'a' in y)

#Identity operator
a = 'Hello'
b = 'hello'
c = 234
d = 432
print("a is b : ", a is b)
print("c is d : ", c is not d)