import time
import board
import digitalio

class coenLED:
    
    def __init__(self,GP=board.GP0):
        self.led = digitalio.DigitalInOut(GP)
        self.led.direction = digitalio.Direction.OUTPUT
    
    
    def on(self):
        '''turns on the lights'''
        self.led.value=True
        
    def off(self):
        '''turns off the lights'''
        self.led.value=False
        
    def on_off(self):
        self.led.value=True
        time.sleep(0.5)
        self.led.value=False
        time.sleep(0.5)