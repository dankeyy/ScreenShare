from main_app.signin import SignIn
from ui_setup.initial_screen_ui import InitialScreenUi


class InitialScreen(object):

    def __init__(self):
        self.main_window = InitialScreenUi()
        self.main_window.show()

        self.main_window.signin_button.clicked.connect(self.open_sign_in_window)
        self.main_window.signup_button.clicked.connect(self.open_sign_up_window)
        self.main_window.exit_button.clicked.connect(self.main_window.close)

    def open_sign_in_window(self):
        """
        Opens Up The Sign In Window
        :return: None
        """
        self.main_window.close()
        self.sign_in_window = SignIn()

    def open_sign_up_window(self):
        """
        Opens Up The Sign Up Window
        :return: None
        """
        pass  # TODO ADD SIGN-UP WINDOW + DATABASE SUPPORT
