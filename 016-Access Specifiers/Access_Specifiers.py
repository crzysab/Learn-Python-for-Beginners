class John():
    def __init__(self):
        self.__pri = "I am private"
        self._pro = "I am protected"
        self.pub = "I am public"

    def some(self): #private variable only access by method
        print("My private variable : ", self.__pri)

obj = John()
print("Protected : ", obj._pro)
print("Public : ", obj.pub)
obj.some()
