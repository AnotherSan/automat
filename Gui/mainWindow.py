from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QComboBox, QDialog, QGridLayout, \
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QSizePolicy, QTableWidget, QVBoxLayout, QGraphicsLayout, QHeaderView, QTableWidgetItem, QWidget, QButtonGroup


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.setWindowTitle("Утюг")
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon(r'Images\presentation.png'))
        self.setWindowFlags(self.windowFlags()
                            | QtCore.Qt.WindowMinimizeButtonHint
                            | QtCore.Qt.WindowMaximizeButtonHint)

        self.create_top_left_group_box()
        self.create_bottom_left_tab_widget()
        self.Red()
        self.Green()

        self.GreenLight.hide()

        main_layout = QGridLayout()
        main_layout.addWidget(self.bottom_left_tab_widget, 1, 1, 3, 3)
        main_layout.addWidget(self.top_left_group_box, 1, 0, 1, 1)
        main_layout.addWidget(self.RedLight, 2, 0, 3, 1)
        main_layout.addWidget(self.GreenLight, 2, 0, 3, 1)
        main_layout.setRowStretch(1, 1)
        main_layout.setRowStretch(2, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)

    def create_bottom_left_tab_widget(self):
        self.bottom_left_tab_widget = QGroupBox()
        self.label=QLabel()
        self.label.setStyleSheet("QLabel{{border-image: url({});}}".format('./images/IronButton.jpg'))
        graphic_h_box = QHBoxLayout()
        graphic_h_box.addWidget(self.label)
        self.bottom_left_tab_widget.setLayout(graphic_h_box)


    def create_top_left_group_box(self):
        self.top_left_group_box = QGroupBox()
        self.button=QPushButton()
        self.button.setText("Включить")
        self.button.clicked.connect(self.Green)

        self.button1=QPushButton()
        self.button1.setText("Выключить")
        self.button1.clicked.connect(self.Red)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addStretch(1)
        self.top_left_group_box.setLayout(layout)

    def Red(self):
        self.RedLight=QGroupBox()
        self.red = QLabel()
        self.red.setStyleSheet("QLabel{{border-image: url({});}}".format('./images/Red.png'))
        self.red.setFixedWidth(60)
        self.red.setFixedHeight(60)
        self.redLayout = QHBoxLayout()
        self.redLayout.addWidget(self.red)
        self.RedLight.setLayout(self.redLayout)
        self.RedLight.show()

    def Green(self):
        self.GreenLight=QGroupBox()
        self.green = QLabel()
        self.green.setStyleSheet("QLabel{{border-image: url({});}}".format('./images/Green.png'))
        self.green.setFixedWidth(60)
        self.green.setFixedHeight(60)
        self.greenLayout = QHBoxLayout()
        self.greenLayout.addWidget(self.green)
        self.GreenLight.setLayout(self.greenLayout)
        self.GreenLight.show()

    #def createAnimation(self):
    #    self.createAnim=QGroupBox("Состояние")
    #    if self.button.event(QtCore.QEvent.MouseButtonPress):
    #        self.createAnim.setLayout(self.greenLayout)
    #    elif self.button1.event(QtCore.QEvent.MouseButtonPress):
    #        self.createAnim.setLayout(self.redLayout)








