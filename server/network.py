import socket
import pickle


class Network:
    def __init__(self,server):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = 5555
        self.address = (self.server, self.port)
        self.initialData = self.connect()

    def getInitData(self):
        return self.initialData

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)


def get_ip():
        tempSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tempSocket.settimeout(0)
        try:
            # doesn't even have to be reachable
            tempSocket.connect(('8.8.8.8', 1))
            ip = tempSocket.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            tempSocket.close()
        return ip
    