# # #libraries
# # import tkinter as tk
# # from tkinter import *

# # class gui2223:
# #     def __init__(self, top=None):

# #         #configures top level
# #         top.geometry("600x450+715+158")
# #         top.minsize(128, 1)
# #         print("blue")
# #         top.maxsize(1924, 1061)
# #         top.resizeable(1, 1)
# #         top.title("main")
# #         top.configure(background="#000000")
# #         top.configure(highlighbackground="#d9d9d9")
# #         top.configure(highlightcolor="black")

# #         print("blue")

# #         #creates top level
# #         self.top

# #         #assigns attributes to self(top level)
# #         self.textBox = Text(top, width=22, height=30)
# #         self.textBox.place(relx=0.8, rely=0.064)
# #         self.textBox.insert(1.0, "Our tasks:\n")

# #         print("blue")
# #land test
# #libraries

# import numpy as np
# import cv2
# import math
# from PIL import Image, ImageFilter
# import matplotlib.pyplot as plt
# import time
# import os
# import tkinter as tk
# from tkinter import *
# import pyautogui as pg
# import pygetwindow


# class guitest:
# video = cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")

# if (video.isOpened() == False):
#     print("Error opening the video file")

# while(video.isOpened()):
#     ret, frame = video.read()
#     if ret == True:
#         # Using waitKey to display each frame of the video for 1 ms
#         #cv2.imshow('Frame',frame)
#         key = cv2.waitKey(1)
#         if key == ord('q'):
#              break
#         # Get the current frame size
#         height, width, _ = frame.shape
#         # Resize the frame
#         scale_percent = 50
#         new_width = int(width * scale_percent / 120)
#         new_height = int(height * scale_percent / 150)
#         dim = (new_width, new_height)
#         resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

#         # Display the resized frame
#         #cv2.imshow('Resized Frame', resized)
        
#         video_bars = cv2.line(resized, (80, 310), (162, 310), (0, 0, 255), 10) 

#         video_two_bars = cv2.line(video_bars, (295, 310), (377, 310), (0, 0, 255), 10)
#         cv2.imshow('with 2 bars', video_bars)

#         # # Define a function for taking screenshot
#         def screenshot():
#             #window = pygetwindow.getWindowsWithTitle('frame')[0]
#             #left, top = window.topleft
#             #right, bottom = window.bottomright
#             random = int(time.time())
#             video = cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")
#             ss = pg.screenshot(video)
#             ss.show()
#             tk.deiconify()
#             # window = pygetwindow.getWindowsWithTitle('frame')[0]
#             # left, top = window.topleft
#             # right, bottom = window.bottomright
#             # random = int(time.time())
#             # filename = "D:/screenshots/" + str(random) + ".jpg" #cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")
#             # pg.screenshot(filename)
#             # ss = Image.open(filename)
#             # ss = ss.crop((left, top, right, bottom))
#             # ss.save(filename)
#             # ss.show()
#             # tk.deiconify()

#         root = tk.Tk()
#         def hide_window():
#             # hiding the tkinter window while taking the screenshot
#             root.withdraw()
#             root.after(1000, screenshot)

#         # # Add a Label widget
#             tk.Label(tk, text="Click the Button to Take the Screenshot", font=('Times New Roman', 18, 'bold')).pack(pady=10)

#         # # Create a Button to take the screenshots #VIDEO STOPS MOVING WHEN THESE LINES ARE INCLUDED
#         button = tk.Button(root, text="Take Screenshot", font=('Aerial 11 bold'), background="#aa7bb1", foreground="white", command=hide_window)
#         button.pack(pady=20)

#         # Wait for a key press
#         k = cv2.waitKey(1) & 0xff
#         root.mainloop()
#         if k == ord('q'):
#             break
 
# cv2.destroyAllWindows()

# #cv2.imshow("image", image)
# #cv2.waitKey(0)
# #cv2.destroyAllWindows()

# #resizing
# #image = cv2.imread('C:/Users/rosar/Pictures/bloopbloop.jpeg', cv2.IMREAD_UNCHANGED)
# #print('Original Dimensions : ',image.shape)
# #width = 380
# #height = 450
# #dim = (width, height)
# #resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# #print('Resized Dimensions : ',resized.shape)

# #rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# #rotated_resized = cv2.resize(rotated_image, dim, interpolation = cv2.INTER_AREA)


# #line_image = cv2.line(rotated_resized, (100, 210), (155, 210), (0, 0, 255), 10) 

# #two_bars = cv2.line(line_image, (210, 210), (265, 210), (0, 0, 255), 10)
# #cv2.imshow('with 2 bars', two_bars)

# #cv2.waitKey(0)
# #cv2.destroyAllWindows()
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
        root = tk.Tk()
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

        canvas1 = tk.Canvas(root, width = 300, height = 300)
        canvas1.pack()

        # # Define a function for taking screenshot
        def screenshot():
            myScreenshot = pg.screenshot()
            myScreenshot.save('screenshot.png')

        def hide_window():
            # hiding the tkinter window while taking the screenshot
            root.withdraw()
            root.after(1000, screenshot)

        # # Add a Label widget
            #tk.Label(tk, text="Click the Button to Take the Screenshot", font=('Times New Roman', 18, 'bold')).pack(pady=10)

        # # Create a Button to take the screenshots #VIDEO STOPS MOVING WHEN THESE LINES ARE INCLUDED
        # myButton = tk.Button(text='Take Screenshot', command=screenshot, bg='green',fg='white',font= 10)
        # canvas1.create_window(150, 150, window=myButton)
        # if key == ord('q'):
        #      break

        # Wait for a key press
        k = cv2.waitKey(1) & 0xff
        root.mainloop()
        if k == ord('q'):
            break
 
cv2.destroyAllWindows()



