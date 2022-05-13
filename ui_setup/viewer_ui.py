from PyQt5 import QtWidgets


class ViewerUi(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScreenShare")
        self.showFullScreen()
