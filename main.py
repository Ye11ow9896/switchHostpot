import sys
from PyQt5.QtWidgets import QApplication
from first import First

class Main(object):
    def __init__(self):
        super().__init__()
        self.first = First()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Main()
    sys.exit(app.exec_())