
import setup
import RoboPiLib as RPL

motorL = 0
motorR = 2

right = 17
front = 16
left = 19

rgo = 2000
lgo = 1000


RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorL, lgo)
RPL.servoWrite(motorL, lgo)
while True:
    RPL.servoWrite(motorR, rgo)
    RPL.servoWrite(motorL, lgo)
    print "-----------"

    while RPL.digitalRead(front) == 0: # something ahead, turn until nothing
        RPL.servoWrite(motorL, rgo)
        print RPL.digitalRead(front)
        if RPL.digitalRead(front) != 0: # nothing to side, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print RPL.digitalRead(front)
            break

    while RPL.digitalRead(right) == 0: # something to right...
        print RPL.digitalRead(right)
        RPL.servoWrite(motorL, rgo) # pivot
        if RPL.digitalRead(right) != 0: # nothing to side, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print RPL.digitalRead(right)
            break

    while RPL.digitalRead(left) == 0: # something to left...
        print RPL.digitalRead(left)
        RPL.servoWrite(motorR, lgo) # pivot
        if RPL.digitalRead(left) != 0: # nothing to side, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print RPL.digitalRead(left)
            break
