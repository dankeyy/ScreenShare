from mss import mss
import socket
import cv2


class Sharer(object):

    def __init__(self, viewer_addr):
        self.viewer_addr = viewer_addr
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((socket.gethostbyname(socket.gethostname()), 8886))

        self.start_work()

    """def send_image(self):
        while self:
            mss().shot(mon=1, output='screen.png')
            with open('screen.png', 'rb') as img:
                image_chunks = img.read(8192)
                while image_chunks:
                    self.s.sendto(image_chunks, (self.viewer_addr, 8886))
                    image_chunks = img.read(8192)
                self.s.sendto(b"DONE", (self.viewer_addr, 8886))"""

    def start_work(self):
        while True:
            mss().shot(output="img.png")
            img = cv2.imread("img.png")
            img_resized = cv2.resize(img, (1080, 720))
            cv2.imwrite("img.png", img_resized)

            with open('img.png', 'rb') as screen_image:
                img_data = screen_image.read(8192)
                while img_data:
                    self.s.sendto(img_data, (self.viewer_addr, 8886))
                    img_data = screen_image.read(8192)
                self.s.sendto("Image sent!".encode('utf-8'), (self.viewer_addr, 8886))
                screen_image.close()
