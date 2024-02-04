#land test
#libraries
import numpy as np
import cv2
import math
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

video = cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")

if (video.isOpened() == False):
    print("Error opening the video file")

while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        # Using waitKey to display each frame of the video for 1 ms
        #cv2.imshow('Frame',frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
             break
        # Get the current frame size
        height, width, _ = frame.shape
        # Resize the frame
        scale_percent = 50
        new_width = int(width * scale_percent / 120)
        new_height = int(height * scale_percent / 150)
        dim = (new_width, new_height)
        resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

        # Display the resized frame
        #cv2.imshow('Resized Frame', resized)
        
        video_bars = cv2.line(resized, (80, 310), (162, 310), (0, 0, 255), 10) 

        video_two_bars = cv2.line(video_bars, (295, 310), (377, 310), (0, 0, 255), 10)
        cv2.imshow('with 1 bars', video_bars)

        # Wait for a key press
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
 
cv2.destroyAllWindows()

#cv2.imshow("image", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#resizing
#image = cv2.imread('C:/Users/rosar/Pictures/bloopbloop.jpeg', cv2.IMREAD_UNCHANGED)
#print('Original Dimensions : ',image.shape)
#width = 380
#height = 450
#dim = (width, height)
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#print('Resized Dimensions : ',resized.shape)

#rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
#rotated_resized = cv2.resize(rotated_image, dim, interpolation = cv2.INTER_AREA)


#line_image = cv2.line(rotated_resized, (100, 210), (155, 210), (0, 0, 255), 10) 

#two_bars = cv2.line(line_image, (210, 210), (265, 210), (0, 0, 255), 10)
#cv2.imshow('with 2 bars', two_bars)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

