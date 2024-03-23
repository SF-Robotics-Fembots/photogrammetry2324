#libraries
from tkinter import *
import tkinter as tk
import cv2
import pyautogui as py
import numpy as np

# creates a Tk() object
master = tk.Tk()
 
# sets the geometry of main 
# root window
master.geometry("450x640")
 
def showCamera():
    video = cv2.VideoCapture(r"C:/Users/rosar\Downloads/IMG_7709.MOV")

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

def photo_image(img):
    h, w = img.shape[:2]
    data = f'P6 {w} {h} 255 '.encode() + img[..., ::-1].tobytes()
    return PhotoImage(width=w, height=h, data=data, format='PPM')

cap = cv2.VideoCapture(r"C:/Users/rosar\Downloads/IMG_7709.MOV")
def update():
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
    if ret1:
        photo = photo_image(np.hstack((img1, img2)))
        canvas.create_image(0, 0, image=photo, anchor=NW)
        canvas.image = photo
    root.after(15, update)

root = Tk()
root.title("Video")
cap1 = cv2.VideoCapture(r"C:/Users/rosar\Downloads/IMG_7709.MOV")
cap2 = cv2.VideoCapture(r"C:/Users/rosar\Downloads/IMG_7709.MOV")

canvas = Canvas(root, width=1200, height=700)
canvas.pack()
#update()
root.mainloop()
cap.release()
 
# function to open a new window 
# on a button click
def openNewWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("450x640")
 
    # A Label widget to show in toplevel
    tk.Label(newWindow, 
          text ="This is a new window").pack()
 
 
label = tk.Label(master, 
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a 
# new window on button click
btn = tk.Button(master, 
             text ="Click to open a new window", 
             command = openNewWindow)
btn.pack(pady = 10)

#vid = tk.Frame()
 
# mainloop, runs infinitely
master.mainloop()