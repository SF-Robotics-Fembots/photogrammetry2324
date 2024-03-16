# # from tkinter import *
# # import time
# # from PIL import ImageTk, Image
import pyautogui as pg
# # import cv2
# import tkinter as tk
# from PIL import Image, ImageTk
import cv2
import tkinter as tk


root = tk.Tk() # create a Tk root window
master = tk.Tk()

w = 400 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#name video variable
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
        print("new wdith, new hgiht", new_width, new_height)

        video_bars = cv2.line(resized, (80, 310), (162, 310), (0, 0, 255), 10) 

        video_two_bars = cv2.line(video_bars, (295, 310), (377, 310), (0, 0, 255), 10)
        cv2.imshow('with 2 bars', video_two_bars)

        #canvas1 is the window that has the ss button
        canvas1 = tk.Canvas(width = 300, height = 300)
        canvas1.pack()

        #if q is pressed, stop program
        if key == ord('q'):
             break
        
        #ss function
        def screenshot():
            #trying to get region of video window
            x, y = root.winfo_x(), root.winfo_y()
            w, h = root.winfo_width(), root.winfo_height()
            #geometry_string = root.geometry()
            #print("geometry_string", geometry_string)
            pg.screenshot('screenshot.png', region=(x, y, w, h))
            myScreenshot = pg.screenshot()
            myScreenshot.save('screenshot.png')
            print("*******************x y w h ", x, y, w, h)

        def hide_window():
            # hiding the tkinter window while taking the screenshot
            root.withdraw()
            root.after(1000, screenshot)

        # # Add a Label widget
            tk.Label(tk, text="Click the Button to Take the Screenshot", font=('Times New Roman', 18, 'bold')).pack(pady=10)


        # # # Create a Button to take the screenshots 
        myButton = tk.Button(text='Take Screenshot', command=screenshot, bg='green',fg='white',font= 10)
        canvas1.create_window(150, 150, window=myButton)

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

cv2.destroyAllWindows()