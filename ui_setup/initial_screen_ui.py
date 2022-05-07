from PyQt5 import QtCore, QtWidgets


class InitialScreenUi(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(850, 500)
        self.setMinimumSize(QtCore.QSize(850, 500))
        self.setMaximumSize(QtCore.QSize(850, 500))
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")

        self.signin_button = QtWidgets.QPushButton(self.central_widget)
        self.signin_button.setGeometry(QtCore.QRect(290, 230, 111, 41))
        self.signin_button.setObjectName("signin_button")

        self.signup_button = QtWidgets.QPushButton(self.central_widget)
        self.signup_button.setGeometry(QtCore.QRect(450, 230, 111, 41))
        self.signup_button.setObjectName("signup_button")

        self.exit_button = QtWidgets.QPushButton(self.central_widget)
        self.exit_button.setGeometry(QtCore.QRect(360, 310, 131, 31))
        self.exit_button.setObjectName("exit_button")

        self.headline = QtWidgets.QTextBrowser(self.central_widget)
        self.headline.setGeometry(QtCore.QRect(110, 100, 641, 91))
        self.headline.setObjectName("headline")

        self.version = QtWidgets.QTextBrowser(self.central_widget)
        self.version.setGeometry(QtCore.QRect(0, 0, 141, 31))
        self.version.setObjectName("version")

        self.setCentralWidget(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.re_translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ScreenShare"))
        self.signin_button.setText(_translate("MainWindow", "Sign In"))
        self.signup_button.setText(_translate("MainWindow", "Sign Up"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.headline.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600;\">ScreenShare</span></p></body></html>"))
        self.version.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#c80623;\">Alpha 0.1</span></p></body></html>"))
