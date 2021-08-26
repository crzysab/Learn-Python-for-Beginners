x = int(input("Input X : "))
y = int(input("Input Y : "))
z = int(input("Input Z : "))

if(x==y) :
    if(x==z):
        print("x is equal to y and z")
    else:
        print("x is equal to y but not equal to z")
elif(x!=y):
    if(x==z):
        print("x not equal to y but equal to z")
    else:
        print("nothing equals")