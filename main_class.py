from App.client import Client
from PyQt5.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = Client()
    sys.exit(app.exec_())
