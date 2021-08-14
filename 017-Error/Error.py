#Compile time error : missing ':' in statement
#Handle Runtime error : user input wrong input value
a = 4
b = 0
try:
    print(a/b)
except Exception:
    print("You cannot divide any number with zero")