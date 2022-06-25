import socket
import sys
FORMAT = "utf-8"
SIZE = 2048

ClientMultiSocket = socket.socket()
host = '192.168.56.103'
port = 2004
print('Waiting for connection response')

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(2048)

while True:
    try:
        mainmenu=ClientMultiSocket.recv(SIZE)   #recv 1
        print(mainmenu.decode(FORMAT))

        Input = input('\nChoose mathematical function: ') #option
        ClientMultiSocket.send(str.encode(Input)) #send 2

        if Input == '4':
            break
        else:

            fnum =input('Enter a number: ')
            ClientMultiSocket.send(str.encode(fnum)) #number

            ans = ClientMultiSocket.recv(SIZE)
            print(ans.decode(FORMAT))

    except KeyboardInterrupt:
        print('\nCtrl + C is pressed, Lost Connection')
        sys.exit()

ClientMultiSocket.close()
