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
        cv2.imshow('with 2 bars', video_bars)

        # # Define a function for taking screenshot
        def screenshot():
            #window = pygetwindow.getWindowsWithTitle('frame')[0]
            #left, top = window.topleft
            #right, bottom = window.bottomright
            random = int(time.time())
            video = cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")
            ss = pg.screenshot(video)
            ss.show()
            tk.deiconify()
            # window = pygetwindow.getWindowsWithTitle('frame')[0]
            # left, top = window.topleft
            # right, bottom = window.bottomright
            # random = int(time.time())
            # filename = "D:/screenshots/" + str(random) + ".jpg" #cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")
            # pg.screenshot(filename)
            # ss = Image.open(filename)
            # ss = ss.crop((left, top, right, bottom))
            # ss.save(filename)
            # ss.show()
            # tk.deiconify()

        root = tk.Tk()
        def hide_window():
            # hiding the tkinter window while taking the screenshot
            root.withdraw()
            root.after(1000, screenshot)

        # # Add a Label widget
            tk.Label(tk, text="Click the Button to Take the Screenshot", font=('Times New Roman', 18, 'bold')).pack(pady=10)

        # # Create a Button to take the screenshots #VIDEO STOPS MOVING WHEN THESE LINES ARE INCLUDED
        button = tk.Button(root, text="Take Screenshot", font=('Aerial 11 bold'), background="#aa7bb1", foreground="white", command=hide_window)
        button.pack(pady=20)
        if key == ord('q'):
             break

        # Wait for a key press
        k = cv2.waitKey(1) & 0xff
        root.mainloop()
        if k == ord('q'):
            break
 
cv2.destroyAllWindows()

