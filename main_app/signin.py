from PyQt5 import QtCore, QtWidgets
from app.client import Client

# UNFINISHED


class SignIn(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def connect(self):
        usr_input, psw_input = self.username_input.toPlainText(), self.password_input.toPlainText()
        if usr_input == '111' and psw_input == '111':
            self.close()
            self.client_window = Client()
            self.client_window.show()

    def setup_ui(self):
        self.setObjectName("signin_window")
        self.resize(450, 300)
        self.setMinimumSize(450, 300)
        self.setMaximumSize(450, 300)

        self.headline = QtWidgets.QTextBrowser(self)
        self.headline.setGeometry(QtCore.QRect(120, 50, 221, 31))
        self.headline.setObjectName("ScreenShare - SignIn")

        self.updated_version = QtWidgets.QTextBrowser(self)
        self.updated_version.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.updated_version.setObjectName("updated_version")

        self.username_input = QtWidgets.QTextEdit(self)
        self.username_input.setGeometry(QtCore.QRect(210, 100, 131, 31))
        self.username_input.setObjectName("username_input")

        self.password_input = QtWidgets.QTextEdit(self)
        self.password_input.setGeometry(QtCore.QRect(210, 140, 131, 31))
        self.password_input.setObjectName("password_input")

        self.username_text = QtWidgets.QTextBrowser(self)
        self.username_text.setGeometry(QtCore.QRect(120, 100, 91, 31))
        self.username_text.setObjectName("username_text")

        self.password_text = QtWidgets.QTextBrowser(self)
        self.password_text.setGeometry(QtCore.QRect(120, 140, 91, 31))
        self.password_text.setObjectName("password_text")

        self.connect_button = QtWidgets.QPushButton(self)
        self.connect_button.setGeometry(QtCore.QRect(240, 200, 81, 31))
        self.connect_button.setObjectName("connect_button")
        self.connect_button.clicked.connect(self.connect)

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setGeometry(QtCore.QRect(140, 200, 81, 31))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.close)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("signin_window", "ShareScreen - Sign In"))
        self.headline.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">ScreenShare SignIn</span></p></body></html>"))
        self.updated_version.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#c81201;\">Alpha 0.1</span></p></body></html>"))
        self.username_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Username:</span></p></body></html>"))
        self.password_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Password:</span></p></body></html>"))
        self.connect_button.setText(_translate("Form", "Connect"))
        self.exit_button.setText(_translate("Form", "Exit"))
