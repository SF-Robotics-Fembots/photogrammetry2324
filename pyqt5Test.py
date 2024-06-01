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
import numpy as np

# cv2.namedWindow("photogrammetry")
# video = cv2.VideoCapture(0)

# #create main window object
# class MainWindow(QWidget):
#     def __init__(self):
#         # video = cv2.VideoCapture[0]
#         super(MainWindow, self).__init__()

#         #create layout for q widget
#         self.VBL = QVBoxLayout()

#         self.FeedLabel = QLabel()
#         self.VBL.addWidget(self.FeedLabel)

#         self.CancelBTN = QPushButton("Cancel")

#         #define worker1 thread in main program
#         self.Worker1 = Worker1()

#         self.Worker1.start()
#         self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
#         self.setLayout(self.VBL)
        
#     #change the pixmap displayed by feed label to value emmitted by worker1 (qthread)
#     def ImageUpdateSlot(self, Image):
#         self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

# #makes connection with camera and captures vid
# class Worker1(QThread):
#     ImageUpdate = pyqtSignal(QImage)
#     #define run function
#     def run(self):
#         self.ThreadActive = True
#         #capture video
#         ret, frame = video.read()
#         while self.ThreadActive:
#             if cv2.waitKey(1) == ord('q'):
#                     break
#             if video.isOpened() == False:
#                  print("Failed to open video")

#             while ret:
#                 Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 FlippedImage = cv2.flip(Image, 1)
#                 ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
#                 Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
#                 #emit thread
#                 self.ImageUpdate.emit(Pic)
#                 bar = cv2.line(frame, (280, 200), (280, 300), (0, 255, 0,), 5)
#                 bar2 = cv2.line(frame, (355, 200), (355, 300), (0, 255, 0,), 5)
#                 cv2.imshow("photogrammetry", bar)
#                 cv2.imshow("photogrammetry", bar2)

#     def stop(self):
#         self.ThreadActive = False
#         self.quit()

# #initialize q main window
# if __name__ == "__main__":
#     App = QApplication(sys.argv)
#     Root = MainWindow()
#     Root.show()
#     sys.exit(App.exec())
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

class MainWindow(QWidget):
     def __init__(self):
         super(MainWindow, self).__init__()
         self.VBL = QVBoxLayout()
         self.FeedLabel = QLabel()
         self.VBL.addWidget(self.FeedLabel)
         self.Worker1 = Worker1()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            if vc.isOpened(): # try to get the first frame
                rval, frame = vc.read()
            else:
                rval = False
            if rval:
                cv2.imshow("preview", frame)
                rval, frame = vc.read()
                key = cv2.waitKey(20)
                if key == 27: # exit on ESC
                    break
                else:
                    cv2.line(frame, (280, 200), (280, 300), (0, 255, 0,), 5)
                    cv2.line(frame, (355, 200), (355, 300), (0, 255, 0,), 5)


vc.release()
cv2.destroyWindow("preview")   