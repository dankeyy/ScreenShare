from PyQt5 import QtCore, QtWidgets


class Client(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("ClientWindow")
        self.resize(950, 700)
        self.setMinimumSize(QtCore.QSize(800, 600))

        self.user_id = QtWidgets.QTextBrowser(self)
        self.user_id.setEnabled(True)
        self.user_id.setGeometry(QtCore.QRect(200, 200, 171, 31))
        self.user_id.setObjectName("user_id")

        self.user_psw = QtWidgets.QTextBrowser(self)
        self.user_psw.setEnabled(True)
        self.user_psw.setGeometry(QtCore.QRect(200, 240, 171, 31))
        self.user_psw.setObjectName("user_psw")

        self.input_psw = QtWidgets.QTextBrowser(self)
        self.input_psw.setEnabled(True)
        self.input_psw.setGeometry(QtCore.QRect(190, 470, 171, 31))
        self.input_psw.setObjectName("input_psw")

        self.input_id = QtWidgets.QTextBrowser(self)
        self.input_id.setEnabled(True)
        self.input_id.setGeometry(QtCore.QRect(190, 430, 171, 31))
        self.input_id.setObjectName("input_id")

        self.id_ver = QtWidgets.QTextBrowser(self)
        self.id_ver.setGeometry(QtCore.QRect(390, 200, 381, 31))
        self.id_ver.setObjectName("id_ver")

        self.psw_ver = QtWidgets.QTextBrowser(self)
        self.psw_ver.setGeometry(QtCore.QRect(390, 240, 381, 31))
        self.psw_ver.setObjectName("psw_ver")

        self.id_edit = QtWidgets.QTextEdit(self)
        self.id_edit.setGeometry(QtCore.QRect(380, 430, 381, 31))
        self.id_edit.setObjectName("id_edit")

        self.psw_edit = QtWidgets.QTextEdit(self)
        self.psw_edit.setGeometry(QtCore.QRect(380, 470, 381, 31))
        self.psw_edit.setObjectName("psw_edit")

        self.connect_button = QtWidgets.QPushButton(self)
        self.connect_button.setGeometry(QtCore.QRect(360, 540, 251, 51))
        self.connect_button.setObjectName("connect_button")

        self.headline = QtWidgets.QTextBrowser(self)
        self.headline.setGeometry(QtCore.QRect(210, 100, 551, 71))
        self.headline.setObjectName("headline")

        self.headline_2 = QtWidgets.QTextBrowser(self)
        self.headline_2.setGeometry(QtCore.QRect(250, 330, 471, 71))
        self.headline_2.setObjectName("headline_2")

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ClientWindow", "ScreenShare"))
        self.user_id.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ID Verification</span></p></body></html>"))
        self.user_psw.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Password Verification</span></p></body></html>"))
        self.input_psw.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Password Verification</span></p></body></html>"))
        self.input_id.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ID Verification</span></p></body></html>"))
        self.connect_button.setText(_translate("ClientWindow", "Connect"))
        self.headline.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">ScreenShare - Client</span></p></body></html>"))
        self.headline_2.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Establish Connection</span></p></body></html>"))
