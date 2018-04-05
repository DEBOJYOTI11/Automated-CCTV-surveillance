# Automated CCTV sureveillence

The project is still under development.

## Introduction

The issue of mass surveillance in CCTV camera feed is very important. Surveillance can be of
different forms like malicious activity detection, identification of a particular entity particular
individual in a CCTV video) or in general keeping tracks of movements of human beings. In our
project, the focus has been given to find the trajectory/path of human through the grid of CCTV
cameras also known as tracking. Also, manually doing tracking can be very difficult and
therefore we present to you our AI based solution that is capable to do this on its own. This is
done with the help of face recognition plus video processing.
Current system in this field aims to search for an entity in video by extracting its face and
matching (or running) it against a database of human faces that is in the interest. So, none of the
systems solve the task if they do not have a predefined database against whom the matching is
done. Our, Smart AI will do this in a smart way by first generating datasets from human faces
taken from CCTV video and use it in a Face Recognition model we are using.
The use of deep learning libraries like Keras along with some image processing tools like
openCV with a cloud based solution is done to achieve this task.
Keywords: Automated tracking, Convolutional-Neural-Network, face recognition.

### Prerequisites

Please take a look at the slides and Report for more information.


### Required packages

* Python3
* OpenCV
* Keras
* Flask
* SQlite or MySQL


### Using Face recognition model
```
Run FaceRecog.ipynb for looking at the original VGG model
```

```
Run FaceRecog_TransfererLearning.ipynb for our model ( VGG model with transfer learning)
```
Both the model use a face dataset for experimentation. Please it here [Face94](http://cswww.essex.ac.uk/mv/allfaces/faces94.html) and place in the project folder where the model in kept. 

### Running client side CCTV application 

![alt text](https://raw.githubusercontent.com/DEBOJYOTI11/Automated-CCTV-surveillance/master/workflow%20diagram.PNG)

Go to the ClientSideCCTV folder and Run 
``` 
Python main.py
```

This should launch the client side system. 
By default it uses the footage form Computer webCam.

``` 
Images with unique identifier are generated in the RecognizedFaces folder.
```

### Running the Server

Configure flask in apache for Google Cloud or Aws and run 

Server/Server Code.py file. 

Configuring is required only for deplyment is cloud (Centralised server). If you are running locally then normal 
```
python Server/Server Code.py is suffient
```
**Linking our Centralised server to the Face Recognition model, so that our main logic could work is unser progress.**
**After the linking is done appropriate analytics can be generated.**

### Possible errors
* Keras not installed ( Keras with Tensorflow)


## Deployment

We have used Google cloud free tier service for deployment. 

## Authors

* **Debojyoti Paul** - *Initial work* - [PurpleBooth](https://github.com/debojyoti11)
* **Bhaskar Sarkar** - *Initial work* 


