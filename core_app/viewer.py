from ui_setup.viewer_ui import ViewerUi


class Viewer(object):

    def __init__(self):
        self.window = ViewerUi()
        self.window.show()

    def share_screen(self):
        self.window.display_image(r"C:\Users\omere\PycharmProjects\ScreenShare\c.JPG")
