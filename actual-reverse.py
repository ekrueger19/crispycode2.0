import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

#Nothing there? Go straight!
while RPL.digitalRead(16) == 1:
    RPL.servoWrite(0, 1000)
    RPL.servoWrite(2, 2000)
    print "all good!"
    #Something there? Back up!
    while RPL.digitalRead(16) == 0:
        future = time.time() + 1
        while time.time() < future:
            RPL.servoWrite(0, 2000)
            RPL.servoWrite(2, 1000)
            print "backin' up!"
            while time.time() >= future:
                #Something still there? Keep Going!
                while RPL.digitalRead(24) == 0:
                    while RPL.digitalRead(17) == 0:
                        future = time.time() + 1
                        while time.time() < future:
                            RPL.servoWrite(0, 2000) # motors reverse
                            RPL.servoWrite(2, 1000)
                            print "back up some more"
                            while time.time() >= future:
                                RPL.servoWrite(0, 0)
                                RPL.servoWrite(2, 0)
                                print "stop"
