#libraries
from PyQt5 import *
import cv2
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np

#create main window object
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        #create layout for q widget
        self.VBL = QVBoxLayout()

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

    #change the pixmap displayed by feed label to value emmitted by worker1 (qthread) 
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
        cv2.destroyAllWindows()

#makes connection with camera and captures vid
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    #define run function
    def run(self):
        self.ThreadActive = True
        #capture video
        video = cv2.VideoCapture(1)
        # Read logo and resize 
        logo = cv2.imread(r'C:/Users/rosar/Downloads/red.png.png') 
        size = 180
        logo = cv2.resize(logo, (size, size)) 
        # Create a mask of logo 
        img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY) 
        ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY) 
        while self.ThreadActive:
            if cv2.waitKey(1) == ord('q'):
                    break
            ret, frame = video.read()
            # Region of Image (ROI), where we want to insert logo 
            roi = ((frame[-size-150:-150, -size-10:-10]), (frame[-size-150:-150, -size-100:-100]))
            #roi1 = roi + (frame[-size-150:-150, -size-100:-100])
            # Set an index of where the mask is 
            roi[np.where(mask)] = 0
            roi += logo 
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