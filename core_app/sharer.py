from mss import mss
import socket


class Sharer(object):

    def __init__(self, viewer_addr):
        self.viewer_addr = viewer_addr
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((socket.gethostbyname(socket.gethostname()), 8886))

        self.send_image()

    def send_image(self):
        mss().shot(mon=1, output='screen.png')
        with open('screen.png', 'rb') as img:
            image_chunks = img.read(2048)
            while image_chunks:
                self.s.sendto(image_chunks, (self.viewer_addr, 8886))
                image_chunks = img.read(2048)
            self.s.sendto(b"DONE", (self.viewer_addr, 8886))
