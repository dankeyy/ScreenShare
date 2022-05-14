import socket
import threading
from ui_setup.client_window_ui import UiClientWindow
from core_app.viewer import Viewer
from core_app.sharer import Sharer


HOST_IP = socket.gethostbyname(socket.gethostname())
CLIENT_IP = "10.0.0.6"
PORT = 8888

# TODO - Get information from a text file until DB is established


class Client(object):

    def __init__(self):
        super().__init__()
        self.main_window = UiClientWindow()
        self.main_window.show()

        self.main_window.connect_button.clicked.connect(self.establish_connection)
        self.thread = threading.Thread(target=self.broadcast_signal)
        self.thread.start()

    def broadcast_signal(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((HOST_IP, 8888))
        while s:
            user_input, addr = s.recvfrom(1024)
            if user_input.decode('utf-8') == 'E97' and self.main_window.isVisible():
                s.sendto(b"Proceed E97", addr)
                s.close()
                self.main_window.close()
                self.sharer = Sharer(addr)

    def establish_connection(self):
        c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        c.sendto(b"E97", (CLIENT_IP, PORT))
        user_input, addr = c.recvfrom(1024)
        if user_input.decode('utf-8') == 'Proceed E97':
            c.close()
            self.main_window.close()
            self.viewer = Viewer()
