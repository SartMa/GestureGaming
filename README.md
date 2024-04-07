
# Gesture Gaming

This project uses a machine learning model to recognize hand gestures in real time, based on which the user can control a game without touching the keyboard.


## Track and Contributors
This project is part of the ML track for Hacknite 2024. The contributors are:

1. Mohammed Ibrahim
2. Sarthak Maheshwari
3. Siddharth Kini
## Problem Statement
The main problem was to identify hand gestures in real time by taking input through a webcam. We needed the model to be accurate and fast. 


## Goal

1.To create a hand gesture detection system, which can then be used in a variety of applications. We applied it to one specific case:
2.To control a game using hand gestures and not using the keyboard (because it is fun).
## Features

1. We used the mobile ssd model for this project. Our model has been trained on over 700 images. It can recognize three kinds of gestures: fist, two, five.
2. The model has very little latency and is very accurate.
3. Our project features a game that we made ourselves in pygame and which can be controlled with hand signs.
4. Our project has a GUI which manages the job of running two windows at once and explains how to control the games to the user, which greatly improves user experience.
## Tech Stack

1. Python
2. Pygame
3. Jupyter Notebook
## How to Run

1. The Tensorflow object API must be installed on your machine. Instructions on how to install it can be found here: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html.
If you are facing problems please downgrade tensorflow to version 2.13 by running the command pip install tensorflow==2.13

2. Download the github repository.

3. Run gui.py in the same environment you downloaded the tensorflow object detection API. Further instructions will be provided there.
## Applications

1. Controlling games
2. It can be used as a sign language interpreter if trained on more data.
## Further Improvements
We can train it for the same gestures using images of different people than ourselves, at different positions and angles, in different environments.

We can also add more gestures so there are more things that can be controlled.
## Demo Video
