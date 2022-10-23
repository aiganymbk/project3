from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout
from instr import *
from second_win import *

def ShowWindow():
    main_win.hide()
    main_win = TestWin()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle(txt_title)
main_win.move(win_x, win_y)
main_win.resize(win_width, win_height)

txt_hello = QLabel(txt_hello)
txt_instruction = QLabel(txt_instruction)
button = QPushButton(txt_next)
button.clicked.connect(ShowWindow)

layout1 = QVBoxLayout()
layout1.addWidget(txt_hello, alignment=Qt.AlignLeft)
layout1.addWidget(txt_instruction, alignment=Qt.AlignLeft)
layout1.addWidget(button, alignment=Qt.AlignLeft)
main_win.setLayout(layout1)

main_win.show()
app.exec_()