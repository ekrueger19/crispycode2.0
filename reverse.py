#If all three sensors are 0, stop then back up then turn 90 degrees then go
import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

#Nothing there? Go straight!
while True:
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
                    while RPL.digitalRead(19) == 0:
                        while RPL.digitalRead(17) == 0:
                            future = time.time() + 0.5
                            while time.time() < future:
                                RPL.servoWrite(0, 2000) # motors reverse
                                RPL.servoWrite(2, 1000)
                                print "back up some more"
                                if time.time() >= future:
                                    RPL.servoWrite(0, 0)
                                    RPL.servoWrite(2, 0)
                                    print "stopping for a moment"
                    while RPL.digitalRead(19) == 0:
                        while RPL.digitalRead(17) == 1:
                            print "nothing to the right"
                            future = time.time() + 2
                            while time.time() < future:
                                RPL.servoWrite(0, 0)
                                RPL.servoWrite(2, 2000)
                                print "turning right"
                                while time.time() >= future:
                                    RPL.servoWrite(0, 2000)
                                    RPL.servoWrite(2, 1000)
                                    print "going forward"
                    while RPL.digitalRead(19) == 1:
                        print "something to the right"
                        while RPL.digitalRead(17) == 0:
                            print "nothing to the left"
                            future = time.time() + 2
                            while time.time() < future:
                                RPL.servoWrite(0, 1000)
                                RPL.servoWrite(2, 0)
                                print "turning left"
                                while time.time() >= future:
                                    RPL.servoWrite(0, 1000)
                                    RPL.servoWrite(2, 2000)
                                    print "going forward"
                        while RPL.digitalRead(17) == 1:
                            future = time.time() + 2
                            while time.time() < future:
                                RPL.servoWrite(0, 1000)
                                RPL.servoWrite(2, 0)
                                print "turning left 2"
                                while time.time() >= future:
                                    RPL.servoWrite(0, 1000)
                                    RPL.servoWrite(2, 2000)
                                    print "going forward"

    while RPL.digitalRead(16) == 0:
        future = time.time() + 3
        while time.time() < future:
            RPL.servoWrite(0, 2000)
            RPL.servoWrite(2, 1000)
            while time.time() >= future:
                while RPL.digitalRead(19) == 0:
                    while RPL.digitalRead(17) == 0:
                        future = time.time() + 3
                        while time.time() < future:
                            RPL.servoWrite(0, 2000)
                            RPL.servoWrite(2, 1000)
                            while time.time() >= future:
                                while RPL.digitalRead(19) == 1:
                                    while RPL.digitalRead(17) == 0:
                                        future = time.time() + 2
                                        while time.time() < future:
                                            RPL.servoWrite(0, 0)
                                            RPL.servoWrite(2, 12000)
                                            if time.time() >= future:
                                                RPL.servoWrite(0, 1000)
                                                RPL.servoWrite(2, 2000)
                                while RPL.digitalRead(19) == 0:
                                    while RPL.digitalRead(17) == 1:
                                        future = time.time() + 2
                                        if time.time() < future:
                                            RPL.servoWrite(2, 0)
                                            RPL.servoWrite(0, 1000)
                                            if time.time() >= future:
                                                RPL.servoWrite(0, 1000)
                                                RPL.servoWrite(2, 2000)
