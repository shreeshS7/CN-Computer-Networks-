import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST = 'localhost'
PORT = 6000

soc = (HOST,PORT)

while True:
    msg = input('[ENTER MESSAGE] : ')
    client.sendto(msg.encode(),soc)
    data,addr = client.recvfrom(1024)
    print('[RECEIVED]',data.decode())
