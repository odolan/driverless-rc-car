import cv2
import numpy as np
#MATPLOT IS NOT WORKING: import matplotlib as plt
import os
import click
import time
import random
import pickle

# lets user see live what the car cam is seeing
def carcam():
    cap = cv2.VideoCapture(-1)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Car Cam', gray)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# failed attempt at collecting data
def collectdata():
    i = 71
    print('Click S to Stop Taking Photos')
    while i < 200:
        time.sleep(.1)
        print('going')

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret == True:
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('/home/pi/DriveCar/photos/image'+str(i)+'.png',grey)
            i = i+1
        else:
            pass
    print('done')

    
            
          
