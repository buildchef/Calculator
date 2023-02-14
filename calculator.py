import sys
from os import system

from PyQt5.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                             QPushButton, QWidget)

system('cls')

# Creatting the Calculator class


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(600, 600)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
