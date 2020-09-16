# SurveillenceSystem
 Due to an increase in robbery cases in ATM kiosks ,It is necessary to increase its  security. This can be achieved by an automated surveillance system.Currently what happens is there is a camera that is attached to the ATM unit that records the video and sent it to the main server of the bank.Early detection of unwanted situations is necessary for taking preventive measures, for which, round the clock surveillance system should work properly by utilizing minimum bandwidth and power. In this project we are going to propose a methodology which is capable of detecting  following activities :
Detecting Human inside the ATM
Multiple person detection in ATM
Camera Covering
Masked face detection.
If a person is taking more than usual time to complete his/her work.

The Complete Life Cycle model is discussed for the Unwanted Activity Detection System. The intended users for this project are banks which can incorporate this project with their CCTV cameras. 

in this project we are going to propose a methodology which is capable of detecting  following activities :
1.Detecting Human inside the ATM
2.Multiple person detection in ATM
3.Camera Covering
4.Masked face detection.
5.If a person is taking more than usual time to complete his/her work.

Detecting Human Inside the ATM and Multiple person detection is done in detection.py.
Masked face detection is done in IIVPFirstReview.ipynb

.We have used keras an open source python library for developing deep learning models.Following are few notable points in this approach:-
1.The sequential keras model has been implemented here.
2.You must have Tensorflow installed and configured at the backend.The other alternative is Theano.Also scipy(along with numpy) must be installed.
3.The dataset that we have used for training here is this.There is not much MAFA(Masked face dataset) is available online.
4.Google colab has been used


The steps that we have followed here are as follows.
1.First mount the drive into google colab
2.Extract the data set into the runtime environment.
3.Execute each step in the google colab after importing the necessary libraries.
4.After the model is fitted and trained go to the next step
5.Now a google api is used to capture the image from the webcam that has been taken from here.once the image is captured it is resized to 150*150(cause is the size of the image with which we have trained the model and pass it to predictFromImage(img) function that will give the score like 1 is for masked and 0 for unmasked.




