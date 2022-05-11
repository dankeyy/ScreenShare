import socket
import threading
from ui_setup.client_window_ui import UiClientWindow

CLIENT_IP = ""
CLIENT_PORT = 8888
LOCAL_IP = ""
LOCAL_PORT = 8886

# TODO - Get information from a text file until DB is established


class Client(object):

    def __init__(self):
        super().__init__()
        self.main_window = UiClientWindow()
        self.main_window.show()

        self.main_window.connect_button.clicked.connect(self.establish_connection)
        self.thread = threading.Thread(target=self.broadcast_signal)
        self.thread.daemon = True
        self.thread.start()

    def broadcast_signal(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((LOCAL_IP, LOCAL_PORT))
            while s:
                print(f"{s.recvfrom(1024)}")

    def establish_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
            c.sendto(b"Hello Host", (CLIENT_IP, CLIENT_PORT))
