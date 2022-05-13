from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap


class ViewerUi(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScreenShare")
        self.showFullScreen()

    def display_image(self, img_dir):
        self.setPixmap(QPixmap(img_dir))
