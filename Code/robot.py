# Testimport
import RPi.GPIO as GPIO
import time



def initialize():
    GPIO.setmode(GPIO.BOARD)
    
class motor:
    pin = {1,1,1,1}
    def initialize(self):
        for p in self.pin:
            GPIO.setup(p,GPIO.OUT)    
            GPIO.output(p,GPIO.LOW)
               
        
def main():
    print("Robot Initialize")
    GPIO.setwarnings(False)
    initialize()
    motorbl = motor()
    motorfl = motor()
    motorbr = motor()
    motorfr = motor()
    motorbl.pin = {37,35,33,31}
    motorfl.pin = {40,38,36,32}
    motorbr.pin = {7,11,13,15}
    motorfr.pin = {8,10,12,16}

    motorbl.initialize()
    motorbr.initialize()
    motorfl.initialize()
    motorfr.initialize()




if __name__ =="__main__":
    main()