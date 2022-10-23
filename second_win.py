from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from time import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        # self.connects()
        
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
    def initUI(self):
        self.button1=QPushButton('Далее')
        self.button2=QPushButton('Далее2')
        self.button3=QPushButton('Далее3')
        self.button4=QPushButton('Далее4')
        self.txt1=QLabel(txt_test1)
        self.txt2=QLabel(txt_test2)
        self.txt3=QLabel(txt_test3)
        self.txt4=QLabel('Введите ФИО')
        self.txt5=QLabel('Возраст:')
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt4, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt5, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.button1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.button2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.button3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.button4, alignment=Qt.AlignLeft)
        #self.r_line.addWidget(, alignment=Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    # def connects(self):
    #     button
    
    # def next_click(self):
    #     second_win.hide()
    #     rw = FinaltWin()
# app=QApplication([])
# test_win=TestWin()
# app.exec_()
