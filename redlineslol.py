# import the require packages.
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QGridLayout, QScrollArea, QSizePolicy, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys
import time
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
#gets camera frames
class CaptureCam(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def __init__(self, url):
        super(CaptureCam, self).__init__()
        self.url = url
        self.threadActive = True

    def run(self) -> None:
        capture = cv2.VideoCapture(self.url)

        if capture.isOpened():
            while self.threadActive:
                #
                ret, frame = capture.read()
                if ret:
                    height, width, channels = frame.shape
                    bytes_per_line = width * channels
                    inverted = cv2.flip(frame, 1)
                    cv_rgb_image = cv2.cvtColor(inverted, cv2.COLOR_BGR2RGB)
                    qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                    qt_rgb_image_scaled = qt_rgb_image.scaled(520, 480, Qt.KeepAspectRatio)

                    self.ImageUpdate.emit(qt_rgb_image_scaled)
                else:
                    break
        capture.release()
        self.quit()

    def stop(self) -> None:
        self.threadActive = False

#ui setup
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        #get camera streams
        self.url_1 = 0


        self.list_cameras = {}

        self.camera_1 = QLabel()
        self.camera_1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera_1.setScaledContents(True)
        self.camera_1.setObjectName("Camera_1")
        self.list_cameras["Camera_1"] = "Normal"

        self.QScrollArea_1 = QScrollArea()
        self.QScrollArea_1.setBackgroundRole(QPalette.Dark)
        self.QScrollArea_1.setWidgetResizable(True)
        self.QScrollArea_1.setWidget(self.camera_1)

       
        self.camera1_label = QLabel("BACK GRIPPER", self)
        self.camera1_label.setStyleSheet("color: #F1F6FD")
        self.camera1_label.setAlignment(Qt.AlignCenter)

        #screenshot stuff
        self.SSbutton = QPushButton("                            SCREENSHOT                         ", self)
        self.SSbutton.setToolTip('screenshot')
        self.SSbutton.clicked.connect(self.screen_shot)
        self.SSbutton.setStyleSheet("color: midnightblue; background: #F1F6FD;")
        self.__SetupUI()

        #connects to ImageUpdate to keep updating the frames
        self.CaptureCam_1 = CaptureCam(self.url_1)
        self.CaptureCam_1.ImageUpdate.connect(lambda image: self.ShowCamera1(image))

        #.start() runs the .run() function in CaptureCam that changes frame settings
        self.CaptureCam_1.start()
    def __SetupUI(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.addWidget(self.QScrollArea_1, 0, 0)
        grid_layout.addWidget(self.camera1_label, 1, 0)

        grid_layout.addWidget(self.SSbutton, 4, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        #grid_layout.setRowMinimumHeight(3, 1)
        #grid_layout.setRowMinimumHeight(4, 2)

        self.widget = QWidget(self)
        self.widget.setLayout(grid_layout)

        self.setCentralWidget(self.widget)
        self.setMinimumSize(1570, 1440)
        #self.showMaximized()
        self.setStyleSheet("QMainWindow {background: 'midnightblue';}")

        self.setWindowTitle("CAMERA GUI")

    @QtCore.pyqtSlot()
    def ShowCamera1(self, frame: QImage) -> None:
        self.camera_1.setPixmap(QPixmap.fromImage(frame))


    #screenshot function
    def screen_shot(self):
        random = int(time.time())
        file = "D:/screenshots" + str(random) + ".png"
        window = pygetwindow.getWindowsWithTitle('CAMERA GUI')[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        pg.screenshot(file)
        im = Image.open(file)
        im = im.crop((left, top, right, bottom))
        im.save(file)
        im.show(file)
    def displayBars(self):
        if self.camera_1 == 0:
            cv2.line()

    def close(self, event):
        if self.CaptureCam_1.isRunning():
            self.CaptureCam_1.quit()
        event.accept()


#runs window
def main():
    # Create a QApplication object. It manages the GUI application's control flow and main settings.
    # It handles widget specific initialization, finalization.
    # For any GUI application using Qt, there is precisely one QApplication object
    app = QApplication(sys.argv)
    # Create an instance of the class MainWindow.
    window = MainWindow()
    # Show the window.
    window.show()
    # Start Qt event loop.
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()