
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST='localhost'
PORT=6002
format = 'utf-8'
server.bind((HOST,PORT))

server.listen()
print('[LISTENEING] waiting for connection...')

conn, addr = server.accept()

print('[CONNECTION ESTABLISHED] connected with :',addr )

conn.send(bytes('Welcome client',format))

print('[MESSENGER STARTED]')

while conn:
    x = input('[Send Message] => ')
    conn.send(bytes(x,format))
    if x == 'exit':
        break
    data = conn.recv(1024*1024).decode()
    print('[Received] => ',data)

server.close()
