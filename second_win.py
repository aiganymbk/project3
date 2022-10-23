from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from time import *

class TestWin(QWidget):
    def __init__(self):
        self.set_appear()
        self.initUI()
        # self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
    def initUi(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget('Введите ФИО', alignment=QT.AlignLeft)
        self.l_line.addWidget('Полных лет', alignment=Qt.AlignLeft)
        self.l_line.addWidget(txt_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(button1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(txt_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(button2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(txt_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(button3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(button4, alignment=Qt.AlignLeft)
        #self.r_line.addWidget(, alignment=Qt.AlignRight)
        self.h_line.addWidget(self.l_line)
        self.h_line.addWidget(self.r_line)
        self.setLayout(self.h_line)
    # def connects(self):
    #     button
    
    # def next_click(self):
    #     second_win.hide()
    #     rw = FinaltWin()
