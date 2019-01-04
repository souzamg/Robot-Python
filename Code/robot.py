# Testimport
import RPi.GPIO as GPIO
import time
import curses


steps = [[1,0,0,0] , [1,1,0,0], [0,1,0,0] , [0,1,1,0] , [0,0,1,0] ,[0,0,1,1] , [0,0,0,1] , [1,0,0,1]]
num_steps = 8
steps1 = [[1,0,0,0] , [0,1,0,0] , [0,0,1,0] , [0,0,0,1] ]
num_steps1 = 4

gear = 1
def initialize():
    GPIO.setmode(GPIO.BOARD)
    
class motor:
    pin = [1,1,1,1]
    position = 0
    def initialize(self):
        self.position = 0
        for p in self.pin:
            GPIO.setup(p,GPIO.OUT)    
            GPIO.output(p,GPIO.LOW)

    def movemotor(self,dir):
        if (gear == 1):
            if dir < 0 :
                if self.position > 0:
                    self.position = self.position - 1
                else:
                    self.position = (num_steps - 1)
            else:
                if self.position >= (num_steps - 1):
                    self.position = 0
                else:
                    self.position = self.position  + 1
            for pos in range(0,4):
                if steps[self.position][pos] == 0:
                    GPIO.output(self.pin[pos],GPIO.LOW)
                else:
                    GPIO.output(self.pin[pos],GPIO.HIGH)
        else:
            if dir < 0 :
                if self.position > 0:
                    self.position = self.position - 1
                else:
                    self.position = (num_steps1 - 1)
            else:
                if self.position >= (num_steps1 - 1):
                    self.position = 0
                else:
                    self.position = self.position  + 1
            for pos in range(0,4):
                if steps1[self.position][pos] == 0:
                    GPIO.output(self.pin[pos],GPIO.LOW)
                else:
                    GPIO.output(self.pin[pos],GPIO.HIGH)
               
        
def main():
    print("Robot Initialize\n")
    gear = 1
    GPIO.setwarnings(False)
    initialize()
    motorbl = motor()
    motorfl = motor()
    motorbr = motor()
    motorfr = motor()
    motorbl.pin = [37,35,33,31]
    motorfl.pin = [40,38,36,32]
    motorbr.pin = [7,11,13,15]
    motorfr.pin = [8,10,12,16]
    motorbl.initialize()
    motorbr.initialize()
    motorfl.initialize()
    motorfr.initialize()
    win =curses.initscr()
    win.nodelay(1)
    curses.noecho()
    curses.cbreak()
    win.keypad(True)
    countfr = 0
    countfl = 0
    countbr = 0
    countbl = 0



    char = -1
    while True:
        char = win.getch()
        if char != -1:
            if char == 113: break
            elif char == curses.KEY_RIGHT:
                countfl = -20 
                countbl = -20
                countfr = 20 
                countbr = 20 
                
            elif char == curses.KEY_LEFT:
                countfl = 20 
                countbl = 20
                countfr = -20 
                countbr = -20 
            elif char == curses.KEY_UP:
                countfl = 20 
                countbl = 20
                countfr = 20 
                countbr = 20 
            elif char == curses.KEY_DOWN:
                countfl = -20 
                countbl = -20
                countfr = -20 
                countbr = -20 
            elif char == 49: 
                countfl = 20 
            elif char == 50 :
                countbl = 20 
            elif char == 51 :
                countfr = 20 
            elif char == 52 :
                countbr = 20 
            elif char == 53: 
                countfl = -20 
            elif char == 54 :
                countbl = -20 
            elif char == 55 :
                countfr = -20 
            elif char == 56 :
                countbr = -20 
            elif char == 103: # G
                if gear == 1:
                    gear = 0
                else:
                    gear = 1   
                print ("Gear ", gear)
            else:
                print(char)
        
        if countfr != 0:
            motorfr.movemotor(countfr)
            if countfr < 0:
                countfr = countfr + 1
            elif countfr > 0:
                countfr = countfr - 1

        if countfl != 0:
            motorfl.movemotor(countfl)
            if countfl < 0:
                countfl = countfl + 1
            elif countfl > 0:
                countfl = countfl - 1

        if countbl != 0:
            motorbl.movemotor(countbl)
            if countbl < 0:
                countbl = countbl + 1
            elif countbl > 0:
                countbl = countbl - 1

        if countbr != 0:
            motorbr.movemotor(countbr)
            if countbr < 0:
                countbr = countbr + 1
            elif countbr > 0:
                countbr = countbr - 1
        time.sleep(0.003)
    curses.endwin()
    print("\nRobot Finalized\n")


if __name__ =="__main__":
    main()