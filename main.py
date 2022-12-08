import pytesseract
import sys
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("DocEnhanced.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.texto = QtWidgets.QPushButton(self.centralwidget)
        self.texto.setGeometry(QtCore.QRect(0, 510, 411, 41))
        self.texto.setObjectName("cat")
        self.imagen = QtWidgets.QPushButton(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(410, 510, 391, 41))
        self.imagen.setObjectName("dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.texto.clicked.connect(self.show_texto)
        self.imagen.clicked.connect(self.show_imagen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.texto.setText(_translate("MainWindow", "Texto"))
        self.imagen.setText(_translate("MainWindow", "Imagen"))
    def show_texto(self):
        self.photo.setText(open('Transcription.txt').read())
    def show_imagen(self):
        self.photo.setPixmap(QtGui.QPixmap("DocEnhanced.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ##ui = Ui_MainWindow()
    ##ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
def tesserackWriter():
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   image_path_in_colab = 'DocEnhanced.jpg'
   extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
   print(extractedInformation)
   with open('Transcription.txt', 'w') as f:
       f.write(extractedInformation)



