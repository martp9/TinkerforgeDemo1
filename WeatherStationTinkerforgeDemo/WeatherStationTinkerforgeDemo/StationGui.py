import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

#Font
f1 = QFont('Arial',10)

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        QToolTip.setFont(f1)

        bntQuit = QPushButton('Quit', self)
        bntQuit.move(50,50)
        bntQuit.setToolTip('Quit App')
        bntQuit.clicked.connect(self.quitMe)

        self.setGeometry(0,0,800,600)
        self.setWindowTitle("Tinkerforge Weather Station")
        self.setWindowIcon(QIcon("_bfhlogo.png"))
        self.show()

    def quitMe(self):
        self.close()
        sys.exit(app.exec_())

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_W:
            self.quitMe()