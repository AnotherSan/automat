import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGroupBox, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import os

from PyQt5 import QtGui


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Утюг'
        self.left = 30
        self.top = 30
        self.width = 640
        self.height = 480
        self.imagenumber = 0
        self.initUI()

    def initUI(self):
        self.buttons()
        self.instructions()
        layout = QGridLayout()
        self.setLayout(layout)
        self.label = QLabel(self)

        layout.addWidget(self.label,1,1,3,3)
        layout.addWidget(self.groupButtons,1,0,1,1)
        layout.addWidget(self.instruct, 2, 0, 3, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("images\\старые\\presentation.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.showimage(0)
        self.show()

    def buttons(self):
        self.groupButtons = QGroupBox()
        self.button = QPushButton()
        self.button.setText("Включить/Выключить")
        self.button.setFont(QtGui.QFont("SansSerif", 11))
        self.button.setCheckable(True)
        self.button.clicked[bool].connect(self.setStateOn)

        self.button1 = QPushButton()
        self.button1.setText("Пар")
        self.button1.setFont(QtGui.QFont("SansSerif", 11))
        self.button1.setCheckable(True)
        self.button1.clicked[bool].connect(self.setStateSteam)

        self.button2 = QPushButton()
        self.button2.setText("Изменить режим")
        self.button2.setFont(QtGui.QFont("SansSerif", 11))
        self.button2.setCheckable(True)
        self.button2.clicked[bool].connect(self.setStateHeat)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.button)
        layout1.addWidget(self.button1)
        layout1.addWidget(self.button2)
        layout1.addStretch(1)
        self.groupButtons.setLayout(layout1)

    def instructions(self):
        self.instruct=QGroupBox()
        self.label1=QLabel()
        self.label1.setText("""Режим отпаривания:\nСерый - Пара нет\nЗеленый - Пар есть\n
        Режимы нагрева:\nЖелтый - Слабый нагрев\nКрасный - Сильный нагрев""")
        self.label1.setFont(QtGui.QFont("SansSerif", 14))
        layout2 = QVBoxLayout()
        layout2.addWidget(self.label1)
        layout2.addStretch(1)
        self.instruct.setLayout(layout2)

    def showimage(self,img):
        directory = "C:\\Users\\Человек\\PycharmProjects\\automatVizualization\\images"
        imagelist = os.listdir(directory)
        pixmap = QPixmap(directory + '\\' + imagelist[img])

        self.imagenumber = img
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width() + 500, pixmap.height())

    def setStateOn(self, pressed):
        count = 0
        if pressed:
            count = + 1
        if count%2 == 0:
            self.showimage(0)
        else:
            self.showimage(1)

    def setStateSteam(self):
        if self.imagenumber != 0 and self.imagenumber != 3 and self.imagenumber != 4:
            if self.imagenumber != 1:
                self.showimage(1)
            else:
                self.showimage(2)

        if self.imagenumber != 0 and self.imagenumber != 1 and self.imagenumber != 2:
            if self.imagenumber != 3:
                self.showimage(3)
            else:
                self.showimage(4)

    def setStateHeat(self):
        if self.imagenumber != 0 and self.imagenumber != 2 and self.imagenumber != 4:
            if self.imagenumber != 1:
                self.showimage(1)
            else:
                self.showimage(3)

        if self.imagenumber != 0 and self.imagenumber != 1 and self.imagenumber != 3:
            if self.imagenumber != 2:
                self.showimage(2)
            else:
                self.showimage(4)





