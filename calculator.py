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

        # Adding buttons
        # first line
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1,
                     lambda: self.display.setText(''))

        # second line
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1)

        # third line
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton('()'), 3, 4, 1, 1)

        # fourth     line
        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton('%'), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1, self.equals)

        self.setCentralWidget(self.cw)

    # Function to create buttons

    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not function:
            btn.clicked.connect(lambda: self.display.setText(
                self.display.text() + btn.text()))

        else:
            btn.clicked.connect(function)

        if not style:
            btn.setStyleSheet(
                'background: #212133; color: #fff; border: 2px solid #413b66; font-size: 30px; border-radius: 20px')

        else:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    # Function to display the result of the operation
    def equals(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Invalid Account')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
