import time
import board
import digitalio
from coenLED_class import *

led1 = coenLED(board.GP0)
led2 = coenLED(board.GP15)


led1.on_off()
led2.on()
