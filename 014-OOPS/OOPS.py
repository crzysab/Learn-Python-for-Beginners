#Without data
class Hello() : #create class
    def my_method(self): #create method
        print("Hello oops")
        print("Thank you")
        return

MyObj = Hello() #create object
MyObj.my_method()

#With data
class student():
    welcome = 'Hi' #static data

    def __init__(self,name,number):
        self.name = name
        self.number = number

    def display(self):
        print("name of the student : ", self.name)
        print("number of the student : ", self.number)
        print("welcome message : ", self.welcome)
        return

std = student('sabrina','006') #dynamic data
std.display()
