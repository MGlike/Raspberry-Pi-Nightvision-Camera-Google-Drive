import RPi.GPIO as GPIO

def main():
    setVision()    

def setVision():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)   
    GPIO.setup(40, GPIO.OUT)    
    GPIO.output(40, 0)   

if __name__ == '__main__':
    main()
