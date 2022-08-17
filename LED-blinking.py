import RPi.GPIO as GPIO
import time
from tkinter import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
running = True

def blinking():
    if running == True:
        GPIO.output(8, True)
        time.sleep(1)
        GPIO.output(8, False)
        time.sleep(1)
    root.after(10, blinking)
    
def stop():
    global running
    running = False
    GPIO.output(8, True)

root = Tk()
button1 = Button(root, text="Click here to make the LED constantly on", command=stop)
button1.pack()

root.after(10, blinking)
root.mainloop()

GPIO.output(8, False)
    
    
