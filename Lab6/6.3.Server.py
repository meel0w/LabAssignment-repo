import socket
import sys
import math         
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

FORMAT = 'utf-8'
SIZE = 2048

# This Logarithmic function
def log(x):
    return math.log(x)

# This Square Root function
def sqrt(x):
    return math.sqrt(x)

# This Exponential function
def exp(x):
    return math.exp(x)

def start_process(s_sock):
    connection.send(str.encode('Server is working:'))
    while True:

        menu = ( ("\nSelect operation.\n") +
            ("\n1.Logarithmic") +
            ("\n2.Square Root") +
            ("\n3.Exponential") +
            ("\n4.Exit") )
        connection.send(str.encode(menu)) #send 1
        print("Waiting for client's option...")

        try:
            
            op = connection.recv(SIZE) #recv 2
            op = op.decode(FORMAT)
            choice = str(op)

            fnum = connection.recv(SIZE)
            num1 = float(fnum.decode(FORMAT))

            if choice == '1':
                ans = log(num1)
                mystring = "Log value"

            elif choice == '2':
                ans = sqrt(num1)
                mystring = "The square root"

            elif choice == '3':
                ans = exp(num1)
                mystring = "Exponential"

            myans = (str(mystring) + ' = ' + str(ans))
            print ('Done!')

        except:
            #ans = 'Thank you'
            #connection.send(str.encode(exit))
            print(f'[+] {s_addr} Client Disconnected')
            

        if not choice:
            break

        connection.send(str.encode(myans))

    connection.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",2004))                                   
    print("waiting...")
    s.listen(5)                                         
    
    try:
        while True:
            try:
                connection, s_addr = s.accept()
                p = Process(target=start_process, args=(connection,))
                p.start()

            except socket.error:

                print('socket error!')

            except Exception as e:        
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()