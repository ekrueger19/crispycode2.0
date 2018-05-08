# Welcome to Ding 3!
# This is wall evasion, with a bonus feature:
# will continue to turn for a minumum of 1 second after a wall is no longer sensed
# what does this do?
# means we hit less walls
# yay

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
lgo = 200


RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorL, lgo)
RPL.servoWrite(motorL, lgo)
while True:
    RPL.servoWrite(motorR, rgo)
    RPL.servoWrite(motorL, lgo)
    print ".............."

    while RPL.digitalRead(front) == 0 and RPL.digitalRead(right) == 0: # reverse
        if RPL.digitalRead(left) == 0:
            RPL.servoWrite(motorR, lgo)
            RPL.servoWrite(motorL, rgo)


    while RPL.digitalRead(front) == 0: # something ahead, turn until nothing
        RPL.servoWrite(motorL, rgo)
        print "++++++"
        if RPL.digitalRead(front) != 0: # nothing to side, go
            now = time.time()
            future = now + 1
            while True:
                if time.time() > future:
                    RPL.servoWrite(motorR, rgo)
                    RPL.servoWrite(motorL, lgo)
                    break
            print "============="
            break

    while RPL.digitalRead(right) == 0: # something to right...
        print "llllllllllllll"
        RPL.servoWrite(motorL, rgo) # pivot
        if RPL.digitalRead(right) != 0: # nothing to side, go
            now = time.time()
            future = now + 1
            while True:
                if time.time() > future:
                    RPL.servoWrite(motorR, rgo)
                    RPL.servoWrite(motorL, lgo)
                    break
            print ":::::::::::"
            break

    while RPL.digitalRead(left) == 0: # something to left...
        print "ooooooooooo"
        RPL.servoWrite(motorR, lgo) # pivot
        if RPL.digitalRead(left) != 0: # nothing to side, go
            now = time.time()
            future = now + 1
            while True:
                if time.time() > future:
                    RPL.servoWrite(motorR, rgo)
                    RPL.servoWrite(motorL, lgo)
                    break
            print "mmmmmmmmmmmmmm"
            break
