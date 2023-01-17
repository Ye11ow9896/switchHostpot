from PyQt5.QtWidgets import (QWidget, QLabel, QMessageBox, QPushButton, QGridLayout, QScrollArea, QMainWindow, QCommandLinkButton, QInputDialog, QApplication, QCheckBox)
from PyQt5.QtCore import Qt
from cons import Connections

class First(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello my friend!")
        self.resize(350, 150)


        self.centralWidget = QWidget(self)
        self.mainlayout = QGridLayout(self.centralWidget)

        ### added label
        self.labellayout = QGridLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Make your choise!")
        self.labellayout.addWidget(self.label, 0, 0, 1, 1)

        ### added buttons
        self.buttonLayout = QGridLayout()
        self.hostpot_btn = QPushButton('Hostpot')
        self.hostpot_btn.clicked.connect(self.hostpot_clicked)
        self.connections_btn = QPushButton('Connections')
        self.connections_btn.clicked.connect(self.connections_clicked)
        self.buttonLayout.addWidget(self.hostpot_btn, 0, 0, 1, 1)
        self.buttonLayout.addWidget(self.connections_btn, 0, 1, 1, 1)

        self.mainlayout.addLayout(self.labellayout, 0, 0, 1, 1)
        self.mainlayout.addLayout(self.buttonLayout, 1, 0, 1, 1)
        self.setCentralWidget(self.centralWidget)
        self.show()
    
    def hostpot_clicked(self):
        pass

    def connections_clicked(self):
        self.cons = Connections()
        self.cons.show()