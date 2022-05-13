from PyQt5 import QtCore, QtWidgets


class UiClientWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("ClientWindow")
        self.setFixedSize(QtCore.QSize(1000, 800))

        self.user_id = QtWidgets.QTextBrowser(self)
        self.user_id.setEnabled(True)
        self.user_id.setGeometry(QtCore.QRect(230, 210, 191, 31))
        self.user_id.setObjectName("user_id")

        self.user_psw = QtWidgets.QTextBrowser(self)
        self.user_psw.setEnabled(True)
        self.user_psw.setGeometry(QtCore.QRect(230, 250, 191, 31))
        self.user_psw.setObjectName("user_psw")

        self.input_psw = QtWidgets.QTextBrowser(self)
        self.input_psw.setEnabled(True)
        self.input_psw.setGeometry(QtCore.QRect(220, 550, 191, 31))
        self.input_psw.setObjectName("input_psw")

        self.input_id = QtWidgets.QTextBrowser(self)
        self.input_id.setEnabled(True)
        self.input_id.setGeometry(QtCore.QRect(220, 510, 191, 31))
        self.input_id.setObjectName("input_id")

        self.id_ver = QtWidgets.QTextBrowser(self)
        self.id_ver.setGeometry(QtCore.QRect(420, 210, 381, 31))
        self.id_ver.setObjectName("id_ver")

        self.psw_ver = QtWidgets.QTextBrowser(self)
        self.psw_ver.setGeometry(QtCore.QRect(420, 250, 381, 31))
        self.psw_ver.setObjectName("psw_ver")

        self.id_edit = QtWidgets.QTextEdit(self)
        self.id_edit.setGeometry(QtCore.QRect(410, 510, 381, 31))
        self.id_edit.setObjectName("id_edit")

        self.psw_edit = QtWidgets.QTextEdit(self)
        self.psw_edit.setGeometry(QtCore.QRect(410, 550, 381, 31))
        self.psw_edit.setObjectName("psw_edit")

        self.connect_button = QtWidgets.QPushButton(self)
        self.connect_button.setGeometry(QtCore.QRect(390, 620, 251, 51))
        self.connect_button.setObjectName("connect_button")

        self.headline = QtWidgets.QTextBrowser(self)
        self.headline.setGeometry(QtCore.QRect(140, 90, 721, 71))
        self.headline.setObjectName("headline")

        self.headline_2 = QtWidgets.QTextBrowser(self)
        self.headline_2.setGeometry(QtCore.QRect(140, 410, 721, 71))
        self.headline_2.setObjectName("headline_2")

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 161, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.re_translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ClientWindow", "Form"))
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
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#c80000;\">Screen</span><span style=\" font-size:36pt; font-weight:600; color:#8704c8;\">Share</span><span style=\" font-size:36pt; font-weight:600;\"> - Client</span></p></body></html>"))
        self.headline_2.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#08c835;\">Establish</span><span style=\" font-size:36pt; font-weight:600;\"> </span><span style=\" font-size:36pt; font-weight:600; color:#0755c8;\">Connection</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("ClientWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#c80230;\">Alpha 0.1</span></p></body></html>"))
