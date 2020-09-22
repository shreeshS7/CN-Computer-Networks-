import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST = 'localhost'
PORT = 6000

soc = (HOST,PORT)
server.bind(soc)
print("[LISTENING]...")
data,addr = server.recvfrom(1024)
print('[RECEIVED]',data.decode())

file_name = input('Enter file name to send :')
server.sendto(file_name.encode(),addr)
file = open(file_name,'rb')
data = file.read()
print('[SENDING FILE] :',file_name)
data = bytes(data)
server.sendto(data,addr)
