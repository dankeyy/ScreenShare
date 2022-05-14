from ui_setup.viewer_ui import ViewerUi
import socket
import threading


class Viewer(object):

    def __init__(self):
        self.window = ViewerUi()
        self.window.show()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((socket.gethostbyname(socket.gethostname()), 8886))
        self.thread = threading.Thread(target=self.display_screen)
        self.thread.start()

    def display_screen(self):
        while self:
            with open('client_screen.png', 'wb') as img:
                print(self.s.recvfrom(2048))
                # image_chunks = self.s.recvfrom(2048)[0]
                while image_chunks:
                    img.write(image_chunks)
                    image_chunks = self.s.recvfrom(2048)[0]
            self.window.display_image('client_screen.png')
