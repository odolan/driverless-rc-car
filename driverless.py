# python3 /home/pi/DriveCar/driverless.py

import RPi.GPIO as gpio 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy
import cv2
import time
import keycontrol as k

CATEGORIES = ['forward','left','right','stop']

print('Starting to load model')
model = load_model('/home/pi/DriveCar/NuralModel1.h5')
print('Done')

cap = cv2.VideoCapture(0)

print('starting to take photos')


for i in range(30):
       ret, frame = cap.read()
       print('now')
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imwrite('/home/pi/DriveCar/carview.png',gray)
       img_array = cv2.imread('/home/pi/DriveCar/carview.png', cv2.IMREAD_GRAYSCALE)
       new_array = cv2.resize(img_array, (38,38))
       cropped = new_array[18:38, 0:38]
       sam = cropped.reshape(-1, 20,38,1)
       X = sam/255.0
       prediction = model.predict([X])
       lookarray = prediction
       print(prediction)
       if lookarray[0][0] > lookarray[0][1] and lookarray[0][0] > lookarray[0][2] and lookarray[0][0] > lookarray[0][3]:
              print('Forward')
              k.forward(.25)
       if lookarray[0][1] > lookarray[0][0] and lookarray[0][1] > lookarray[0][2] and lookarray[0][1] > lookarray[0][3]:
              print('Left')
              k.left(.25)
       if lookarray[0][2] > lookarray[0][0] and lookarray[0][2] > lookarray[0][1] and lookarray[0][2] > lookarray[0][3]:
              print('Right')
              k.right(.25)
       if lookarray[0][3] > lookarray[0][0] and lookarray[0][3] > lookarray[0][1] and lookarray[0][3] > lookarray[0][2]:
              print('Stop')
              
       print("")
       time.sleep(2)

#use if want to hand feed photo to the network
def prepare(filepath):
       img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
       new_array = cv2.resize(img_array, (38,38))
       cropped = new_array[18:38, 0:38]
       return cropped.reshape(-1, 20,38,1)
       prediction = model.predict([prepare('/home/pi/DriveCar/5.JPG')])
       print(prediction)
   
 
