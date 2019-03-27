import RPi.GPIO as gpio 
import time
#from unicurses import *
import click

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, False)
    gpio.setup(22, False)
    gpio.setup(23, False)
    gpio.setup(24, False)
    
def left(t):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(t)
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(.35)
    gpio.cleanup()
    
def right(t):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(t)
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(.35)
    gpio.cleanup()
    
def forward(t):
    init()
    gpio.output(17, False) 
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, False)
    time.sleep(t)
    gpio.cleanup()

def backward(t):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)
    time.sleep(t)
    gpio.cleanup()

        
def carmove():
    while True:
        key = click.getchar()
        if key == 'w':
            forward(.25)
        if key == 's':
            backward(.25)
        if key == 'a':
            left(.25)
        if key == 'd':
            right(.25)
        if key == 'q':
            break


    
    

    
    
    
