import random
import sys

import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.par = False
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.pushButton = PyQt5.QtWidgets.QPushButton(self)
        self.pushButton.setText('Create')
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.par:
            painter = QPainter(self)
            painter.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            painter.drawEllipse(random.randint(0, 600), random.randint(0, 600), random.randint(0, 600),
                                random.randint(0, 600))
            painter.end()
            self.par = False

    def run(self):
        self.par = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())