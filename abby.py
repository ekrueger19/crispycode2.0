import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now


# MAKE A CODE!
# input a Password
#

lock = 800
step1 = 1300
step2 = 1700
unlock = 3000


RPL.servoWrite(0,lock)
print "Do you want to unlock a safe? Riddle me this:"
print "Why don't you like sand?"

def one():
    p1 = raw_input("One: ")
    if p1 == "It's course":
        RPL.servoWrite(0,step1)
        return True
    elif p1 == "You're going down a path I can't follow":
        print "Ironic."
        return False
    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        return False

def two():
    p2 = raw_input("Two: ")
    if p2 == "rough":
        RPL.servoWrite(0,step2)
        return True
    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        return False

def three():
    p3 = raw_input("Three: ")
    if p3 == "irritating":
        RPL.servoWrite(0,unlock)
        print "And it gets everywhere."
        print "General Kenobi, you are a bold one."
        return True
    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        return False

while True:
    one()
        if one() == False:
            break
        if one() == True:
            two()
    two()
        if two() == True:
            three()
        if two() == False:
            one()
    three()
        if three() == False:
            one()
        if three() == True:
            break
