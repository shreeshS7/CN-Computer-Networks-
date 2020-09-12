import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 6015
format = 'utf-8'
client.connect((HOST,PORT))

while True:
    send = input('[ENTER MESSAGE ] => ')
    send = client.send(bytes(send,format))
    msg = client.recv(1024).decode()
    print('[RECEIVED] => ',msg)
