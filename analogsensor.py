# analog

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

analogR = 5

rgo = 2000
lgo = 1000

while True:
    while RPL.analogRead(analogR) >= 300:
        print "middle"
        print RPL.analogRead(analogR)
    while RPL.analogRead(analogR) < 300:
        while RPL.digitalRead(19) == 0:
            print "close"
            print RPL.analogRead(analogR)
        while RPL.digitalRead(19) == 1:
            print "far"
            print RPL.analogRead(analogR)
        while RPL.analogRead(analogR) >= 550:
            continue
