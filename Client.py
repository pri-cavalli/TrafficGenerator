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
        self.lastMessageLength = self.rate - ((self.packetsPerSecond - 1) * Constants.UDP_DEFAULT_BUFFER_SIZE)

        self.message = bytearray(Constants.UDP_DEFAULT_BUFFER_SIZE)
        self.lastMessage = bytearray(self.lastMessageLength)

    def start(self):
        rateInMbitsPerSecond = self.rate * 8 / 1000000
        print("Enviarei", self.packetsPerSecond, "pacotes por segundo")
        while True:
            timeToWait = 1.0 / float(self.packetsPerSecond)
            remainSecond = 1.0

            for packet in range(0, self.packetsPerSecond):
                timeBegin = time.time()
                
                self.socket.sendto(self.message, (self.ip, self.port))
                time.sleep(timeToWait)

                remainPackets = self.packetsPerSecond - packet
                if remainSecond > 0:
                    timeToWait = remainSecond / float(remainPackets)
                else:
                    timeToWait = 0.0

                timeEnd = time.time()
                remainSecond -= timeEnd - timeBegin 

            if self.lastMessageLength != 0:
                self.socket.sendto(self.lastMessage, (self.ip, self.port))
                time.sleep(timeToWait)

            print("Enviou", rateInMbitsPerSecond, "Mbit/s")
