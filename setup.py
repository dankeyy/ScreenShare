from App.mainwindow import MainWindow
from PyQt5.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = MainWindow()
    client.show()
    sys.exit(app.exec_())
