import socket
from math import *
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 6003
format = 'utf-8'

server.bind((HOST,PORT))
server.listen()
print('[LISTENING]...')

conn,addr = server.accept()

print(f'[ESTABLISHED CONNECTION WITH {addr}]')
conn.send(bytes('Welcome Client',format))

while True:
    calc = conn.recv(1024).decode()
    fun = calc[:3]
    if calc == 'exit':
        break
    if fun == 'sin':
        ans = sin(int(calc[4:-1]))
    elif fun == 'cos':
        ans = cos(int(calc[4:-1]))
    elif fun == 'tan':
        ans = tan(int(calc[4:-1]))
    elif fun == 'cot':
        ans = 1/(tan(int(calc[4:-1])))
    elif fun == 'sec':
        ans = 1/(cos(int(calc[4:-1])))
    elif fun == 'csc':
        ans = 1/(sin(int(calc[4:-1])))
    conn.send(bytes(str(ans),format))
    print(f'[SENT] => {ans}')


conn.close()
server.close()
