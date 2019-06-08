import argparse
import sys

class ClientParser:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", help="IP destino", type=str)
        parser.add_argument("-p", help="Porta", type=int)
        parser.add_argument("-r", help="Tamanho da rajada", type=int)
        self.args = parser.parse_args()

    def getArgs(self):
        return self.args
