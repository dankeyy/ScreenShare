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
        self.thread = threading.Thread(target=self.recv_img)
        self.thread.start()

    """def display_screen(self):
        while self:
            with open('client_screen.png', 'wb') as img:
                image_chunks = self.s.recvfrom(8192)[0]
                while not image_chunks == b"DONE":
                    img.write(image_chunks)
                    image_chunks = self.s.recvfrom(8192)[0]
            self.window.display_image('client_screen.png')
            os.remove('client_screen.png')"""

    def recv_img(self):
        while True:
            rewrite_data = None
            if os.path.isfile('D:\images\img.png'):
                os.remove('D:\images\img.png')
            img = open('D:\images\img.png', 'wb')
            while True:
                data = self.s.recv(8192)
                if rewrite_data is None:
                    rewrite_data = data
                else:
                    rewrite_data = rewrite_data + data
                if "Image sent!".encode('utf-8') in data:
                    img.write(rewrite_data)
                    img.close()

                    self.window.display_image('D:\images\img.png')
                    break
