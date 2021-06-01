from microbit import *

class Scheduler(object):
    def __init__(self, interval):
        self.__interval = interval
        self.__started = False

    def start(self, func):
        self.__func = func
        self.__started = True
        self.__next = running_time() + self.__interval

    def stop(self):
        self.__started = False

    def exec(self):
        if self.__started and running_time() > self.__next:
            self.__next = running_time() + self.__interval
            self.__func()
            return True 
        else:
            return False 

def show_name():
    global name, index
    display.show(name[index])
    index = (index + 1) % len(name)

mydelay = 3
name = "ALEX"
index = 0
display.show("1")

# clear the button pressed state
button_a.was_pressed()
button_b.was_pressed()

# initialize the scheduler
s = Scheduler(mydelay)

while True:
    if button_a.was_pressed():
        display.show("2")
        s.start(show_name)
    if button_b.was_pressed():
        display.show("3")
        s.stop()
    
    if s.exec():
        pass

        