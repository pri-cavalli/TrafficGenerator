import sys
import ClientParser
import Client
import Server

Parser = ClientParser.ClientParser()

def main():
    args = Parser.getArgs()
    print(args.i != None, args.p != None, args.r != None)
    if args.i != None and args.p != None and args.r != None:        
        print("Eu sou o cliente!")
        client = Client.Client(args)
        client.start()
    elif args.p != None:     
        print("Eu sou o servidor!")
        server = Server.Server(args)
        server.start()
    else:
        print("Está faltando argumentos")

if __name__ == '__main__':
    main()
    