import socket
import threading
from ui_setup.client_window_ui import UiClientWindow

LOCAL_IP = ""
LOCAL_PORT = 8888
HOST_IP = ""
HOST_PORT = 8886


class Client(object):

    def __init__(self):
        super().__init__()
        self.main_window = UiClientWindow()
        self.main_window.show()

    def broadcast_signal(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((LOCAL_IP, LOCAL_PORT))
            s.listen(1)
            conn, addr = s.accept()
            print(f"{conn} + {addr}")

    def establish_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
            c.connect((HOST_IP, HOST_PORT))
