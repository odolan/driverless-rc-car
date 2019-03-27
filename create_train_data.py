# takes training data from within folders as classification and adds to
# an array with the grayscale data and classification in array (training_data)
import numpy as np
import os
import time
import cv2
import random
import sys
import codecs
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
sys.stderr.write("\x1b[2J\x1b[H")

class nuralnetwork:
    

    def createtrainingdata():

        import time

        training_data = []

        IMG_SIZE1 = 20 
        IMG_SIZE2 = 38

        DATADIR = '/home/pi/DriveCar/images/'
        CATEGORIES = ['forward','left','right','stop']

        print('whats up')
        for category in CATEGORIES:
            path = os.path.join(DATADIR, category)
            class_num = CATEGORIES.index(category)
            for img in os.listdir(path):
                try:
                    img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                    new_array = cv2.resize(img_array, (38,20))
                    training_data.append([new_array, class_num])
                except Exception as e:
                    pass
            
        #print(len(training_data))
        random.shuffle(training_data)

         # prints out the direction in binary of the first ten shuffled images
        '''for sample in training_data[:10]:
        print(sample[1])'''
        print(len(training_data))
              
        X = []
        y = []

        for features, label in training_data:
            X.append(features)
            y.append(label)

        X = np.array(X).reshape(-1, 20, 38, 1)
        

        print('Done')

        return X, y

        #this sets up the data. From here the nural net takes over in the nural python document

        

    def trainnetwork(X, y):

        NAME = "DirectionNet{}".format(int(time.time()))

        tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))

        X = X/255.0

        model = Sequential()
        model.add(Conv2D(64, (3,3), input_shape = X.shape[1:]))
        model.add(MaxPooling2D(pool_size=(2,2), strides=2))
        model.add(Activation('relu'))
        model.add(Dropout(0.25))
        print('.')

        model.add(Conv2D(64, (3,3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Activation('relu'))
        print('.')

        model.add(Flatten())
        #model.add(Dropout(0.25))
        print('.')

        model.add(Dense(64))
        model.add(Activation('relu'))
        print('.')

        model.add(Dense(4)) 
        model.add(Activation('sigmoid'))
        print('.')

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        testlabels = keras.utils.to_categorical(y, num_classes=4)
        
        print('.')

        model.fit(X, testlabels, batch_size=23, epochs=4, validation_split=0.1)

        #model.save('NuralModel1.h5')

        '''img_array = cv2.imread('/home/pi/DriveCar/5.JPG', cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (38,38))
        cropped = new_array[18:38, 0:38]
        cropped.reshape(-1, 20,38,1)

        prediction = model.predict([cropped])
        print(prediction)'''

        
        




    
    
