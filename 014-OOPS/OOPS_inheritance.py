class animal():
    def eat(self):
        print("Eating : ")
class dog(animal):
    def bark(self):
        print("barking")

d = dog()
d.eat()
d.bark()

