import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Berjaya buat sokett")

port = 8888

s.bind(("", port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("Soket tengah menunggu client!")

while True:
    c, addr = s.accept()
    print("Dapat capaian dari:" + str(addr))
    c.send(b'Terima Kasih!')
    buffer = c.recvfrom(1024)
    print(buffer)
    
c.close()