import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP15)
led2.direction = digitalio.Direction.OUTPUT


led.value = True

led2.value = True

while True:
    led.value = True
    time.sleep(0.5)
    led2.value = False
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    led2.value = True
    time.sleep(0.5)