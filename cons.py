from PyQt5.QtWidgets import (QWidget, QDialog, QLabel, QMessageBox, QPushButton, QGridLayout, QScrollArea, QMainWindow, QCommandLinkButton, QInputDialog, QApplication, QCheckBox)
from PyQt5.QtCore import Qt
import re
import os

class Connections(QDialog):
    def __init__(self):
        super().__init__()
        command = "nmcli device show | grep -P 'GENERAL.DEVICE|GENERAL.TYPE'"
        pipe = os.popen(command)
        s = pipe.read()
        s1 = re.sub("[^A-Za-z | 0-9 | - | :]", "",s)
        s2 = re.sub(r'\s+', '', s1, flags=re.UNICODE)
        text = s2.split("GENERALDEVICE:")
        print(text)
        command = 'iwlist wlxd03745c763fc scan | grep ESSID:'
        pipe = os.popen(command)
        s = pipe.read()
        s1 = re.sub("[^A-Za-z | 0-9 | -]", "",s)
        s2 = re.sub(r'\s+', '', s1, flags=re.UNICODE)
        print(s2)
        text = s2.split("ESSID")
        for i in range(len(text)):
            if text[0] == '':
                text.remove(text[0])
        print(str(text))

        self.resize(300,350)
        self.setWindowTitle("Available connections")
        self.gridLayout = QGridLayout()

        for i in range(len(text)):
            link_btn = QCommandLinkButton()
            self.gridLayout.addWidget(link_btn, i, 0, 1, 2)
            self.str = str(text[i])
            link_btn.ssid = text[i]
            link_btn.setText(self.str)
            link_btn.clicked.connect(self._link_clicked)

        self.setLayout(self.gridLayout)

    def _link_clicked(self):
        ssid = self.sender().ssid
        msg = QMessageBox()
        text, ok = QInputDialog.getText(self, f"Connection {ssid}", "Enter password")
        if ok:
            cmd = f'nmcli device wifi connect {ssid} password {text} | grep successfully'
            self.temp = os.popen(cmd)
            self.answ = self.temp.read()
            if not self.answ == '':
                msg.setText(f'Connecting to {ssid} is successfully!')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                self.close()
            else:
                msg.setText(f'No connection with {ssid}')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        


