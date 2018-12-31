# Testimport
import RPI.GPIO as GPIO
import time



def initialize()
    GPIO.setmode(GPIO.BCM)
    
class motor:
    pin[]={1,1,1,1}
    def initialize()
        GPIO.setup(self.pin[0].GPIO.OUT)
        GPIO.setup(self.pin[1].GPIO.OUT)
        GPIO.setup(self.pin[2].GPIO.OUT)
        GPIO.setup(self.pin[3].GPIO.OUT)
        
        GPIO.output(self.pin[0].GPIO.LOW)
        GPIO.output(self.pin[1].GPIO.LOW)
        GPIO.output(self.pin[2].GPIO.LOW)
        GPIO.output(self.pin[3].GPIO.LOW)
