# python3 /home/pi/DriveCar/nuralnet.py

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import create_train_data

 def trainnetwork():
        
        X = create_train_data.nuralnetwork.createtrainingdata.X

        X = X/255.0


        '''model = Squential()
        model.add(Conv2D(64, (3,3), input_shape = X.shape[1:]))
        model.add(Activation('relu'))
        model.ad(MaxPooling2D(pool_size=(2,2)))

        model.add(Conv2D(64, (3,3)))
        model.add(Activation('relu'))
        model.ad(MaxPooling2D(pool_size=(2,2)))

        model.add(Flatten())

        model.add(Dense(64))
        model.add(Activation('relu'))

        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.compile(loss='categorical_crossentropy',
                  optimiser='adam',
                  metrics=['accuracy'])

        model.fit(X, y, batch_size=23, epochs=3, validation_split=0.1)'''

        print('done')
