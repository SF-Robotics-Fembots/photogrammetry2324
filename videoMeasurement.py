#THIS HAS JUST VIDEO W/ BARS
#land test
#libraries
import numpy as np
import cv2
import math
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import time
import os
import tkinter as tk
from tkinter import *
import pyautogui as pg
import pygetwindow
                                               
video = cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")

if (video.isOpened() == False):
    print("Error opening the video file")

while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        # Using waitKey to display each frame of the video for 1 ms
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
        
        video_bars = cv2.line(resized, (80, 310), (162, 310), (0, 0, 255), 10) 

        video_two_bars = cv2.line(video_bars, (295, 310), (377, 310), (0, 0, 255), 10)
        cv2.imshow('with 2 bars', video_two_bars)

        root = tk.Tk()

        if key == ord('q'):
             break

        # Wait for a key press
        # k = cv2.waitKey(1) & 0xff
        # root.mainloop()
        # if k == ord('q'):
        #     break
 
cv2.destroyAllWindows()

