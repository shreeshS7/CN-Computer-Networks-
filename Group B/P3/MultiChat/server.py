import socket
import _thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 6015
format = 'utf-8'
server.bind((HOST,PORT))
server.listen()
print('[LISTENING ]...')
def new_conn(conn,addr):
    while True:
        print(' ')
        print(f'[SERVING CLIENT {addr} ]')
        data = conn.recv(1024).decode()
        print('[RECEIVED] => ',data)
        if data=='exit':
            conn.send(bytes('[THANKS FOR CONNECTING...]',format))
            break
        conn.send(bytes(input('[ENTER MESSAGE] => '),format))

    conn.close()

while True:
    conn,addr = server.accept()
    _thread.start_new_thread(new_conn,(conn,addr))

server.close()
