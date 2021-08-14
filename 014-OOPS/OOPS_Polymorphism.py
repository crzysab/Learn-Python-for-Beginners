class dog():
    def sound(self):
        print("bow bow")

class cat():
    def sound(self):
        print("miaw miaw")

def makeSound(animaltype):
    animaltype.sound()

d1 = dog()
c1 = cat()

makeSound(d1)
makeSound(c1)