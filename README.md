# driverless-rc-car
By: Owen Dolan 

*There were too many photos to upload the photos to github *
*I used approximatly 10000 photos to train the network*

This can be used in tandem with a raspberry pi and camera to achieve a "driverless car" that follows a path of sticky notes

A video detailing its creation can be found here: https://www.youtube.com/watch?v=s1TXi-oRMOs&t=146s 

NuralModel1.h5 = a pretrained CNN which can be used to drive the car, so retraining is not needed everytime. This model is 
                 however a work in progress. Although it achieved over 80% accuracy.  
                 
                 
camcon.py = a python file which allows a user to view the camera of the pi, or collect images and have them save (one every
            second) for training.                  
            
car.py = a file which allows a developer to perform different actions to the car, such as test driving, controlling by hand,
         or training the nural network automatically. 
         
carview.png = an example image of what the camera is seeing.

create_train_data.py = this is responsible for two functions. The first takes images from folders labeled with directions and
                       turns that into pixel data in an array with corrospondign trainign value. The second function, takes
                       the two arrays that the first function produces, and trains a CNN neural network with it. After
                       training, the model is saved as a .h5 filetype. 
                      
driverless.py = a python script that can be used to completly run the car autonomously based off of the trained .h5 file it 
                reads in. It uses camera data as input.   
                
keycontrol.py = a file that can be used to control the cars movement by using the arrow keys of a computer that is SSH the
                raspberry pi.  
                
nuralnet.py = a python file which trains the neural network.               

WHAT IS NEEDED TO RUN THE CODE:
      A raspberry pi with wifi, a camera that can plug in to the pi by usb or a raspi cam. The pi will need to have python
      3.5, tensorflow, and opencv installed to work (those are the only major packages). Driverless.py and NuralModel1.h5 are
      the only files needed to run this project.  

