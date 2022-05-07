from app.initial_screen import InitialScreen
from PyQt5.QtWidgets import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = InitialScreen()
    sys.exit(app.exec_())
