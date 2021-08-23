#Without parameter
def my_func() : #function declaration
    x = int(input("enter any number (x) : "))
    y = int(input("enter any number (y) : "))
    z = x+y
    print("Result of my_func : ", z)
    return (z) #end of function

my_func() #call function

#With parameter
def my_func2(arg1,arg2) :
    total = arg1 + arg2
    print("total my_func2 : ",total)
    return (total)

my_func2(12,5)