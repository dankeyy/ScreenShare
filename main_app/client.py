import socket
import threading
from ui_setup.client_window_ui import UiClientWindow

CLIENT_IP = "10.0.0.6"
LOCAL_IP = "10.0.0.8"
PORT = 8888

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
            s.bind((LOCAL_IP, PORT))
            while s:
                user_input, addr = s.recvfrom(1024)
                user_input = user_input.decode('utf-8')
                if user_input == 'E97':
                    print(f"Signal Established {addr[0]}")
                    s.sendto(b"Proceed E97", addr)

    def establish_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
            c.sendto(b"E97", (CLIENT_IP, PORT))
            print(c.recvfrom(1024))
