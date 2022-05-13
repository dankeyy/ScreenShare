from ui_setup.viewer_ui import ViewerUi


class Viewer(object):

    def __init__(self):
        self.window = ViewerUi()
        self.window.show()
