from time import *

index = 0

class Scheduler(object):
    def __init__(self, interval):
        self.__interval = interval
        self.__started = False

    def start(self, func):
        self.__func = func
        self.__started = True
        self.__next = time() + self.__interval

    def stop(self):
        self.__started = False

    def exec(self):
        if self.__started and time() > self.__next:
            self.__next = time() + self.__interval
            self.__func()
            return True 
        else:
            return False
name = "Alex"
def show_name():
    global index, name
    s = str.format("Index = {0} Time = {1} Name = {2} \n", index, time(), name[index])
    print(s)
    index = (index + 1) % len(name) 

sc = Scheduler(2)
sc.start(show_name)

while True:
    if sc.exec():
        pass
    