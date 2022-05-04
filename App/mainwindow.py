from PyQt5 import QtCore, QtWidgets
from App.signin import SignIn


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def open_sign_in_window(self):
        """
        Opens Up The Client Window
        :return: None
        """
        self.close()
        self.sign_window = SignIn()
        self.sign_window.show()

    def setup_ui(self):
        """
        Defines The Structure Of Main Window && Functionality
        :return: None
        """
        self.setObjectName("MainWindow")
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.resize(850, 450)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.signin_button = QtWidgets.QPushButton(self.centralwidget)
        self.signin_button.setGeometry(QtCore.QRect(250, 170, 351, 41))
        self.signin_button.setObjectName("signin_button")
        self.signin_button.clicked.connect(self.open_sign_in_window)

        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(250, 230, 351, 41))
        self.settings_button.setObjectName("signin_button_2")
        # Define Function

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(370, 330, 121, 31))
        self.exit_button.setObjectName("signin_button_3")
        self.exit_button.clicked.connect(self.close)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 30, 491, 91))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 91, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        """
        Customizes Structures In Main Window
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ScreenShare"))
        self.signin_button.setText(_translate("MainWindow", "Sign In"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600;\">ScreenShare</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#c80623;\">Alpha 0.1</span></p></body></html>"))
