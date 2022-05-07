from app.signin import SignIn
from ui_setup.initial_screen_ui import InitialScreenUi


class InitialScreen(object):

    def __init__(self):
        self.window = InitialScreenUi()
        self.window.show()

        self.window.signin_button.clicked.connect(self.open_sign_in_window)
        self.window.signup_button.clicked.connect(self.open_sign_up_window)
        self.window.exit_button.clicked.connect(self.window.close)

    def open_sign_in_window(self):
        """
        Opens Up The Sign In Window
        :return: None
        """
        pass

    def open_sign_up_window(self):
        """
        Opens Up The Sign Up Window
        :return: None
        """
        pass  # TODO ADD SIGN-IP WINDOW + DATABASE SUPPORT
