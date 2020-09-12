
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 6002
format = 'utf-8'
server.bind((HOST,PORT))

server.listen()
print('[LISTENING] waiting for connection...')

conn, addr = server.accept()
print('[CONNECTION ESTABLISHED] with ',addr)

conn.send(bytes('Welcome Client',format))

file_name = input('Enter file name to send :')
conn.send(bytes(file_name,format))
file = open(file_name,'r')
data = file.read()
print('[SENDING FILE] :',file_name)
conn.sendall(bytes(str(data),format))

conn.close()
server.close()
