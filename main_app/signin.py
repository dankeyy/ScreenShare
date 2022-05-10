from main_app.client import Client
from ui_setup.signin_ui import SigninUi

# TODO - Connect() => Add DB Communication && Authentication


class SignIn(object):

    def __init__(self):
        super().__init__()
        self.window = SigninUi()
        self.window.show()

        self.window.exit_button.clicked.connect(self.window.close)
        self.window.connect_button.clicked.connect(self.connect)

    def connect(self):
        usr_input, psw_input = self.window.username_input.toPlainText(), self.window.password_input.toPlainText()
        if usr_input == '111' and psw_input == '111':
            self.window.close()
            self.client = Client()
