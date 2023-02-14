import sys
from os import system

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
                             QPushButton, QSizePolicy, QWidget)

system('cls')

# Creatting the Calculator class


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(600, 600)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.list_operators = ['(', '+', '-', '/', '*', '%']
        self.setStyleSheet('background: #161829')

        # Adding a display
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            'background: #212133; color: #fff; font-size: 30px; border-radius: 20px;')
        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
