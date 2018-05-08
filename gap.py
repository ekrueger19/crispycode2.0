import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorR = 2
motorL = 0
# lsens = 23
# fsens = 16

# motorR forward = 1000
# motorL forward = 2000


# Okay so this is good but I think we need to do a thing to actually make it...
# ...turn into a gap because right now it's just turning away from a wall

RPL.servoWrite(motorR,100)
RPL.servoWrite(motorL,2000)
print "going"
while RPL.digitalRead(23) == 0:
    RPL.servoWrite(motorR, 100)
    RPL.servoWrite(motorL, 2000)
    print "something"
    while RPL.digitalRead(23) == 1:
        timeb = time.time()
        RPL.servoWrite(motorR, 100)
        RPL.servoWrite(motorL, 2000)
        print "gap"
        while RPL.digitalRead(23) == 0:
            timea = time.time()
            timeg = timea - timeb
            if timeg < 2:
                RPL.servoWrite(motorR, 100)
                RPL.servoWrite(motorL, 2000)
                print "moving on"
            while timeg >= 2:
                timp = time.time() + timeg
                while time.time() < timp:
                    RPL.servoWrite(motorR, 2000)
                    RPL.servoWrite(motorL, 1000)
                    print "backing up"
                    while time.time() >= timp:
                        timmy = time.time() + 2
                        while time.time() < timmy:
                            RPL.servoWrite(motorR, 0)
                            RPL.servoWrite(motorL, 2000)
                            print "turning in"
                            while time.time() >= timmy:
                                RPL.servoWrite(motorR, 100)
                                RPL.servoWrite(motorL, 2000)
                                print "moving through"
# here I think we should have it drive past the gap with the analog sensors...
# ... on the side and then if it does the thing then yeah
