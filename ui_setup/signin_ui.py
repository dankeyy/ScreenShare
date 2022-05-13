from PyQt5 import QtCore, QtWidgets


class SigninUi(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("SignInWindow")
        self.setFixedSize(QtCore.QSize(450, 300))

        self.headline = QtWidgets.QTextBrowser(self)
        self.headline.setGeometry(QtCore.QRect(80, 50, 300, 30))
        self.headline.setObjectName("headline")

        self.updated_version = QtWidgets.QTextBrowser(self)
        self.updated_version.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.updated_version.setObjectName("updated_version")

        self.username_input = QtWidgets.QTextEdit(self)
        self.username_input.setGeometry(QtCore.QRect(210, 100, 151, 31))
        self.username_input.setObjectName("username_input")

        self.password_input = QtWidgets.QTextEdit(self)
        self.password_input.setGeometry(QtCore.QRect(210, 140, 151, 31))
        self.password_input.setObjectName("password_input")

        self.username_text = QtWidgets.QTextBrowser(self)
        self.username_text.setGeometry(QtCore.QRect(100, 100, 111, 31))
        self.username_text.setObjectName("username_text")

        self.password_text = QtWidgets.QTextBrowser(self)
        self.password_text.setGeometry(QtCore.QRect(100, 140, 111, 31))
        self.password_text.setObjectName("password_text")

        self.connect_button = QtWidgets.QPushButton(self)
        self.connect_button.setGeometry(QtCore.QRect(240, 200, 81, 31))
        self.connect_button.setObjectName("connect_button")

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setGeometry(QtCore.QRect(140, 200, 81, 31))
        self.exit_button.setObjectName("exit_button")

        self.re_translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SignInWindow", "SignInWindow"))
        self.headline.setHtml(_translate("SignInWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">ScreenShare Sign-In</span></p></body></html>"))
        self.updated_version.setHtml(_translate("SignInWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#c81201;\">Alpha 0.1</span></p></body></html>"))
        self.username_text.setHtml(_translate("SignInWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Username:</span></p></body></html>"))
        self.password_text.setHtml(_translate("SignInWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Password:</span></p></body></html>"))
        self.connect_button.setText(_translate("SignInWindow", "Connect"))
        self.exit_button.setText(_translate("SignInWindow", "Exit"))
