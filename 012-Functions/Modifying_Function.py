def div(a,b):
    if(b==0):
        return print("Please enter another number for b")
    else:
        c = a/b
        return print("Result : ",c)

x = input("Enter a  : ")
y = input("Enter b  : ")

div(int(x),int(y))