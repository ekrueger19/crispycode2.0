import setup
import RoboPiLib as RPL
import time

motorR = 2
motorL = 0

while True:
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(motorL, 100)
        RPL.servoWrite(motorR, 2000)
        print "nothing"

    while RPL.digitalRead(16) == 0:
        future = time.time() + 0.5
        while time.time() < future:
            RPL.servoWrite(motorL, 600)
            RPL.servoWrite(motorR, 1500)
            print "slowing"
            while time.time() >= future:
                RPL.servoWrite(motorL, 0)
                RPL.servoWrite(motorR, 0)
                print "stop"
