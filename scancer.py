from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
import os
from imageai.Classification.Custom import CustomImageClassification


class Ui_MainWindow():

    def __init__(self, MainWindow):
        super().__init__()
        #self.MainWindow.setWindowTitle("Cancer App")
        self.setupUi(MainWindow)
    
    def setupUi(self, MainWindow):

        self.FileName = ''
        #MainWindow
        MainWindow.setObjectName("Scancer")
        MainWindow.resize(801, 602)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")

        #CentralWidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 50, 140, 1100))
        self.frame.setStyleSheet("background-color: rgb(18, 106, 1)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #PushButton
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 100, 32))
        font = QtGui.QFont()
        font.setFamily(".Aqua Kana")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-style: outset;\ncolor: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.enterEvent = lambda e: self.pushButton.setStyleSheet("border-style: outset;\ncolor: rgb(0, 255, 94);")
        self.pushButton.leaveEvent = lambda e: self.pushButton.setStyleSheet("border-style: outset;\ncolor: rgb(255, 255, 255);")
        self.pushButton.clicked.connect(self.about)
        print(self.pushButton.styleSheet())

        #PushButton_2
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 100, 32))
        font = QtGui.QFont()
        font.setFamily(".Aqua Kana")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-style: outset;\ncolor: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.enterEvent = lambda e: self.pushButton_2.setStyleSheet("border-style: outset;\ncolor: rgb(0, 255, 94);")
        self.pushButton_2.leaveEvent = lambda e: self.pushButton_2.setStyleSheet("border-style: outset;\ncolor: rgb(255, 255, 255);")
        self.pushButton_2.clicked.connect(self.dev)
        print(self.pushButton_2.styleSheet())

        #Frame_2
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 2000, 50))
        self.frame_2.setStyleSheet("background-color: rgb(35, 176, 3)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        #GraphicsView (logo)
        self.logo = QtWidgets.QPushButton(self.frame_2)
        self.logo.setGeometry(QtCore.QRect(20, 9, 100, 32))
        self.logo.setStyleSheet('border-style: outset')
        self.logo.setObjectName("logo")
        self.logo.clicked.connect(self.home)
        self.logo.setIcon(QIcon('temp.png'))
        self.logo.setIconSize(QSize(120, 120))
        self.logo.show()

        #Frame_3
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(140, 50, 1920, 1080))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.hide()

        #Frame_4
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(140, 50, 1920, 1080))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        #Frame_5
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(140, 50, 1920, 1080))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.hide()

        #Label
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 551))
        self.label.setStyleSheet("margin: 10px\nsetMargin(100);")
        self.label.setObjectName("label")
        self.label.setText('placeholder')

        #FileSelectButton
        self.fileSelectButton = QtWidgets.QPushButton(self.frame_4)
        self.fileSelectButton.setGeometry(QtCore.QRect(0, 0, 661, 350))
        self.fileSelectButton.setText("Click to input file")
        self.fileSelectButton.clicked.connect(self.showFileDialog)
        self.fileSelectButton.setStyleSheet('''
QPushButton {
    color: black;
    background-color: rgb(235, 235, 235)
}
        ''')

        #CalculateButton
        self.calculateButton = QtWidgets.QPushButton(self.frame_4)
        self.calculateButton.setGeometry(QtCore.QRect(0, 350, 60, 30))
        self.calculateButton.setText("Calculate")
        self.calculateButton.setStyleSheet('''
QPushButton {
    color: black;
}
        ''')
        self.calculateButton.setEnabled(False)
        self.calculateButton.clicked.connect(self.calculate)

        #Results
        self.results = QtWidgets.QLabel(self.frame_4)
        self.results.setGeometry(QtCore.QRect(0, 380, 200, 100))

        #Dev
        self.devLabel = QtWidgets.QLabel(self.frame_5)
        self.devLabel.setGeometry(QtCore.QRect(0, 0, 661, 551))
        self.devLabel.setText('Placeholder 2')

        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Scancer", "Scancer"))
        self.pushButton.setText(_translate("Scancer", "About"))
        self.pushButton_2.setText(_translate("Scancer", "Dev"))

    def clickme(self):
        print('pressed')

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            print("Mouse is over the label")
        elif event.type() == QEvent.Leave:
            print("Mouse is not over the label")

    def showFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.frame_4,"Select file", "","All Files (*);;Text Files (*.txt)", options=options)
        self.fileName = fileName
        name, extension = os.path.splitext(fileName)
        if extension.lower() == '.png':
            self.valid_file = True
        else:
            self.valid_file = False
        if self.valid_file:
            self.fileSelectButton.setText("")
            self.fileSelectButton.setIcon(QIcon(QPixmap(fileName)))
            self.fileSelectButton.setIconSize(self.fileSelectButton.sizeHint()*100)
            self.calculateButton.setEnabled(True)
        else:
            self.fileSelectButton.setIcon(QIcon())
            self.fileSelectButton.setText("Only .png files accepted\nClick again to input another file")
            self.calculateButton.setEnabled(False)

    def calculate(self):
        values = ''
        execution_path = os.getcwd()
        prediction = CustomImageClassification()
        prediction.setModelTypeAsResNet50()
        prediction.setModelPath("/Users/Hari/Documents/scancer/trained_model.h5")
        prediction.setJsonPath(os.path.join(execution_path, "Data_model_classes.json"))
        prediction.loadModel()
        predictions, probabilities = prediction.classifyImage(self.fileName, result_count=4)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            if 'adenocarcinoma' in eachPrediction.lower():
                values = values + 'Adenocarcinoma: ' + str(eachProbability) + '\n'
            if 'squamous' in eachPrediction.lower():
                values = values + 'Squamous Cell Carcinoma: ' + str(eachProbability) + '\n'
            if 'large' in eachPrediction.lower():
                values = values + 'Large Cell Carcinoma: ' + str(eachProbability) + '\n'
            if 'normal' in eachPrediction:
                values = values + 'Healthy: ' + str(eachProbability) + '\n'

        self.results.setText(values)

    def about(self):
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_3.show()

    def dev(self):
        self.frame_4.hide()
        self.frame_3.hide()
        self.frame_5.show()

    def home(self):
        self.frame_3.hide()
        self.frame_4.show()
        self.frame_5.hide()
        
        

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
