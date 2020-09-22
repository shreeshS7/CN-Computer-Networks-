import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST = 'localhost'
PORT = 6000

soc = (HOST,PORT)
server.bind(soc)
print("[LISTENING]...")
while True:
    data,addr = server.recvfrom(1024)
    print('[RECEIVED]',data.decode())
    msg = input('[ENTER MESSAGE] : ')
    server.sendto(msg.encode(),addr)
