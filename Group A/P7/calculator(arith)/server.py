import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 6002
format = 'utf-8'
server.bind((HOST,PORT))
server.listen()
print('[LISTENING]')
conn , addr = server.accept()
print(conn)
print('space')
print(addr)
print(f'[CONNECTION ESTABLISHED WITH {addr}] ')

while True:
    cal = conn.recv(1024).decode()
    result = eval(cal)
    conn.send(bytes(str(result),format))
    print(f'[SENDING] {result}')

conn.close()
server.close()
