import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import DocEnhance

frame = None

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        #Video Label
        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        #Boton cancelar
        self.CancelBtn = QPushButton('Cancel')
        self.CancelBtn.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBtn)

        #Boton captura
        self.CapturaBtn = QPushButton('Capturar')
        self.CapturaBtn.clicked.connect(self.Capture)
        self.VBL.addWidget(self.CapturaBtn)

        #Actualizador de video
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
        sys.exit(0)

    def Capture(self):
        self.Worker1.stop()
        cv2.imshow('Enhanced image', DocEnhance.GetImage(frame))

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture('FotosTest/TestVideo.mp4')
        while self.ThreadActive:
            global frame
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
        Capture.release()

    def stop(self):
        self.ThreadActive = False
        self.quit()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec_())
