# Shrishti2017
MaRsModel: Image Processing Work on OpenCv

Introduction:
This program is capable of detecting any object according to the colour range provided ( yellow colour by default).

Other requirement to be satisfied to detect an object are-
1. It must atleast cover area equal to a circle os 10px
2. The object should be in front of camera immediately after running the python program.
3. It will by default capture only one object if multiple objects are brought in front of it. The object detected will cover the largest the area on screen.

File:
The Program of concern or for MaRsModel is test.py, rest of them are usefull programs that helped me for better understanding of openCV.

Install:
To run this program on your system:
Follow this tutorial to install openCV on your system- http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/ (For ubuntu 16.04)

What it does:
Function of this program is to store location of four points in space and perspectively transform the selected points. Movement of object can be detected by a red line vector.
After perspective transformation the recieved co-ordinate of the point will be with respect to the transformed frame.

Working on test.py:
To store co-ordinates for perspective transformation press ('k').Order of storing points should be in clockwise sense starting from bottom-left corner. Stored point will be simultaneously printed on the terminal. to recieve the co-ordinate of the center of the area of object press key ('C')
Again after storing all four point Another frame will appear will transformed live video, and pressing ('c') will print coresponding co-ordinate.
Press ('Q') to exit the program.

Hope it works :P
