# welcome to best.py !
# it is not the best but I love it anyway
# this should be a wall following type thing but be nice to it


# perceived problem: will zig zag


import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorL = 0
motorR = 2

right = 17
front = 16
left = 19

rgo = 2000
rslow = 1500
lgo = 100
lslow = 600


RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorL, lgo)
RPL.servoWrite(motorL, lgo)

while True:
    RPL.servoWrite(motorR, rgo)
    RPL.servoWrite(motorL, lgo)

    while RPL.analogRead(analogR) >= 300: # middle range, can go straight
        print "we good"
        RPL.servoWrite(motorR, rgo)
        RPL.servoWrite(motorL, lgo)

    while RPL.analogRead(analogR) < 300: # no longer middle
        while RPL.digitalRead(19) == 0: # digital also sense, so close
            print "close"
            print RPL.analogRead(analogR)
            RPL.servoWrite(motorR, rslow)
            RPL.servoWrite(motorL, lgo)

        while RPL.digitalRead(19) == 1: # digital doesn't sense, far
            print "far"
            print RPL.analogRead(analogR)
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lslow)
