from abc import ABC,abstractmethod

class animal(ABC):

    @abstractmethod
    def move(self):
        pass

class lion(animal):
    def move(self):
        print("I can walk and run...")

class snake(animal):
    def move(self):
        print("I can crawl only..")

l1 = lion()
l1.move()
s1 = snake()
s1.move()