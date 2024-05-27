#libraries
from PyQt5 import *
from PyQt5 import QtWidgets
import cv2
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
from tkinter import *
import tkinter as tk
import pyautogui as pg
import time
import pygetwindow
from PIL import Image

#create main window object
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        title = "photogrammetry"
        
        #self.setGeometry(0, 0, 500, 300)

        #create layout for q widget
        self.VBL = QVBoxLayout()
        self.setWindowTitle(title)

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")

        self.VBL.addWidget(self.CancelBTN)
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        #define worker1 thread in main program
        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

        self.ssBTN = QPushButton("Screenshot")
        self.VBL.addWidget(self.ssBTN)
        self.ssBTN.clicked.connect(self.screenshot)
        self.VBL.addWidget(self.ssBTN)

    #change the pixmap displayed by feed label to value emmitted by worker1 (qthread) 
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
        time.sleep(0)
        cv2.destroyAllWindows()

    def screenshot(self):
            #titles = pygetwindow.getAllTitles() #prob dont need this
            #random = int(time.time())
            file = 'screenshot.png'
            window = pygetwindow.getWindowsWithTitle('photogrammetry')[0]
            left, top = window.topleft
            right, bottom = window.bottomright
            pg.screenshot(file)
            im = Image.open(file)
            im = im.crop((left+19, top+42, right-19, bottom-106))
            #im.save(file)
            im.show(file)

#makes connection with camera and captures vid
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    #define run function
    def run(self):
        self.ThreadActive = True
        #capture video
        video = cv2.VideoCapture(0)
        # Read logo and resize 
        logo = cv2.imread(r'C:/Users/rosar/Downloads/red.png.png') 
        logo2 = cv2.imread(r'C:/Users/rosar/Downloads/red.png.png')
        size = 180
        logo = cv2.resize(logo, (size, size)) 
        logo2 = cv2.resize(logo2, (size, size))
        # Create a mask of logo 
        img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        img3gray = cv2.cvtColor(logo2, cv2.COLOR_BGR2GRAY) 
        ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
        ret2, mask2 = cv2.threshold(img3gray, 1, 255, cv2.THRESH_BINARY) #probably dont need ret2
        while self.ThreadActive:
            if cv2.waitKey(1) == ord('q'):
                    break
            ret, frame = video.read()
            if video.isOpened() == False:
                 print("Failed to open video")
            # Region of Image (ROI), where we want to insert logo 
            roi = ((frame[-size-150:-150, -size-10:-10]))
            roi2 = ((frame[-size-150:-150, -size-450:-450]))
            #roi1 = roi + (frame[-size-150:-150, -size-100:-100])
            # Set an index of where the mask is 
            roi[np.where(mask)] = 0
            roi2[np.where(mask2)] = 0
            roi += logo
            roi2 += logo2
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                #emit thread
                self.ImageUpdate.emit(Pic)
                
    def stop(self):
        self.ThreadActive = False
        self.quit()

#initialize q main window
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())