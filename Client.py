import socket
import Constants
import math
import time

class Client:

    def __init__(self, args):
        self.ip = args.i
        self.port = args.p
        self.rate = math.ceil(args.r * 1000 / 8)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.packetsPerSecond = math.ceil(self.rate / Constants.UDP_DEFAULT_BUFFER_SIZE)
        self.lastPacketLength = self.rate - ((self.packetsPerSecond - 1) * Constants.UDP_DEFAULT_BUFFER_SIZE)
        

    def start(self):
        timeToWait = 1 / self.packetsPerSecond
        while True:
            for _ in range(self.packetsPerSecond - 1):
                self.socket.sendto(bytearray(Constants.UDP_DEFAULT_BUFFER_SIZE), (self.ip, self.port))
                print("Enviou", Constants.UDP_DEFAULT_BUFFER_SIZE, "bytes")
                time.sleep(timeToWait)
            if self.lastPacketLength != 0:
                self.socket.sendto(bytearray(self.lastPacketLength), (self.ip, self.port))
                print("Enviou", self.lastPacketLength, "bytes")
                time.sleep(timeToWait)