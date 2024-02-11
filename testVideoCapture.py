# from tkinter import *
# import time
# from PIL import ImageTk, Image
# import pyautogui as pg
# import cv2
import tkinter as tk
from PIL import Image, ImageTk
import cv2

# # Create an instance of tkinter frame or window
# win = Tk()

# # Set the size of the window
# win.geometry("700x350")

# # Define a function for taking screenshot
# def screenshot():
#    random = int(time.time())
#    video = cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV")
#    ss = pg.screenshot(video)
#    ss.show()
#    win.deiconify()

# def hide_window():
#    # hiding the tkinter window while taking the screenshot
#    win.withdraw()
#    win.after(1000, screenshot)

# # Add a Label widget
#    Label(win, text="Click the Button to Take the Screenshot", font=('Times New Roman', 18, 'bold')).pack(pady=10)

# # Create a Button to take the screenshots
# button = Button(win, text="Take Screenshot", font=('Aerial 11 bold'), background="#aa7bb1", foreground="white", command=hide_window)
# button.pack(pady=20)

# win.mainloop()
class MainWindow():
    def __init__(self, window, cap):
        self.window = window
        self.cap = cap
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 20 # Interval in ms to get the latest frame
        # Create canvas for image
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0)
        # Update image on canvas
        self.update_image()
    def update_image(self):
        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image)
        # self.canvas = tk.Canvas(self.window, width = self.width, height = self.height)
        # self.canvas.pack()
    def rescale_frame(frame, percent=30):
        width = int(frame.shape[1] * percent / 100)
        height = int(frame.shape[0] * percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root, cv2.VideoCapture(r"C:\Users\rosar\Downloads\IMG_7709.MOV"))
    root.mainloop()