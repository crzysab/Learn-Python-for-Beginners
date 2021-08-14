import threading
from time import *

class Thread1(threading.Thread):
    def run(self):
        for i in range(50):
            print("python")
            sleep(0.2)

class Thread2(threading.Thread):
    def run(self) :
        for i in range(50):
            print("java")
            sleep(2)

t1 = Thread1()
sleep(0.3)
t2 = Thread2()

t1.start()
t2.start()