from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5 import uic
import sys
from random import *


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.c = []

        self.circle_btn.clicked.connect(self.draw_circle)

    def draw_circle(self):
        radius = randint(1, 50)
        x = randint(0, 400)
        y = randint(0, 400)
        self.c.append((x, y, radius))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(QColor(255, 255, 0), 1)
        qp.setPen(pen)
        if self.c:
            for i in range(len(self.c)):
                qp.drawEllipse(self.c[i][0], self.c[i][1], self.c[i][2], self.c[i][2])
        qp.end()


app = QApplication(sys.argv)
ex = Circles()
ex.show()
sys.exit(app.exec_())