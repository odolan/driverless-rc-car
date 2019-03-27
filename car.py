"""To run this file type in (source ~/.profile) wait for it to load
. type workon cv. Then run this: python3 /home/pi/DriveCar/car.py"""

#import nuralnet
import keycontrol
import create_train_data
import camcon
import csv
import click
import sys
import time
from threading import Thread

sys.stderr.write("\x1b[2J\x1b[H")

print("b:test, n:collectdata, m:autonomous, c:format create and train trainnetowrk")
select = click.getchar() 
if select == 'b':
    print('TESTDRIVE')
    time.sleep(1)
    print('Are you using g:Pi or h:PC')
    whatdevice = click.getchar() 
    if whatdevice == 'g':
        sys.stderr.write("\x1b[2J\x1b[H")
        Thread(target = camcon.carcam).start()
        Thread(target = keycontrol.carmove).start()
    if whatdevice == 'h':
        sys.stderr.write("\x1b[2J\x1b[H")
        print('Sorry, cam view not possible')
        keycontrol.carmove()
            
if select == 'n':
    print('Collecting Images')
    time.sleep(.3)
    print('.')
    time.sleep(.3)
    print('.')
    time.sleep(.3)
    print('.')
    camcon.collectdata()
    
if select == 'm':
    print("This feature isnt working yet! please notify the developer")

if select == 'c':
    sys.stderr.write("\x1b[2J\x1b[H")
    print('format data and train data')
    X, y = create_train_data.nuralnetwork.createtrainingdata()
    print('done create data')
    create_train_data.nuralnetwork.trainnetwork(X, y)
    #nuralnet.trainnetwork()
    print('done training data')


    

