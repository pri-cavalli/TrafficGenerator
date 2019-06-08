import socket
import Constants

class Server:

    def __init__(self, args):
        self.port = args.p
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.getOwnIpAdress(), self.port))
        

    def start(self):
        while True:
            print('Received {} bytes from host {}')
            data, address = self.socket.recvfrom(Constants.UDP_DEFAULT_BUFFER_SIZE)
            print('Received {} bytes from host {}'.format(len(data), address))
            

    def getOwnIpAdress(self):
        temporarySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temporarySocket.connect(("8.8.8.8", 80))
        ownIp = temporarySocket.getsockname()[0]
        temporarySocket.close()
        print(ownIp)
        return ownIp