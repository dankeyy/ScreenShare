from ui_setup.viewer_ui import ViewerUi
import socket
import threading
import os


class Viewer(object):

    def __init__(self):
        self.window = ViewerUi()
        self.window.show()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((socket.gethostbyname(socket.gethostname()), 8886))
        self.thread = threading.Thread(target=self.display_screen)
        self.thread.start()

    def display_screen(self):
        with open('client_screen.png', 'wb') as img:
            image_chunks = self.s.recvfrom(2048)[0]
            while not image_chunks == b"DONE":
                img.write(image_chunks)
                image_chunks = self.s.recvfrom(2048)[0]
                print(image_chunks)
        self.window.display_image('client_screen.png')
        # os.remove('client_screen.png')
