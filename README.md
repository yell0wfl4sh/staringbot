# Abstract

MarsMOdel bot is an autonomous object detecting bot. It has the ability to detect the object moving in front of him. It uses Image Processing for detection of object. Motor drivers are used to control the movement of robot. Servos provide movement to head of the bot. A tiny wireless spy camera is mounted on the ceiling. live feed can be seen on the screen to which receiver is connected and tuned. 

# Team Members

Yash Agrawal
Yash Jain
Ujjwal Gupta
Shubham Sharele

# Mentors

Mohit Gupta
Sunil Saini

# Applications

It can be used as a decoration bot. That stares anyone walking in.
It can be used as a Virtual Board. Using the code As it detects a object's movement, It can be used to write on a virtual board.

# Mechanical

Ply board
4 Servo

# Electronics

1 Arduino UNO
Wireless camera

# Electronic Design

Arduino

Arduino is an open source electronics prototyping platform based on flexible, easy to use hardware and software.It’s intended for artists,designers,hobbyists and anyone interested in creating interactive objects or environment.For wireless surveying bot,we used arduino product ‘Arduino UNO’ board.



# Concept

This program is capable of detecting any object according to the colour range provided ( yellow colour by default).

Other requirement to be satisfied to detect an object are-
1. It must atleast cover area equal to a circle os 10px
2. The object should be in front of camera immediately after running the python program.
3. It will by default capture only one object if multiple objects are brought in front of it. The object detected will cover the largest the area on screen.

# File:
The Program of concern or for MaRsModel is test.py, rest of them are usefull programs that helped me for better understanding of openCV.

# Install:
To run this program on your system:
Follow this tutorial to install openCV on your system- http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/ (For ubuntu 16.04)

# What it does:
Function of this program is to store location of four points in space and perspectively transform the selected points. Movement of object can be detected by a red line vector.
After perspective transformation the recieved co-ordinate of the point will be with respect to the transformed frame.

# Working on test.py:
To store co-ordinates for perspective transformation press ('k').Order of storing points should be in clockwise sense starting from bottom-left corner. Stored point will be simultaneously printed on the terminal. to recieve the co-ordinate of the center of the area of object press key ('C')
Again after storing all four point Another frame will appear will transformed live video, and pressing ('c') will print coresponding co-ordinate.
Press ('Q') to exit the program.

