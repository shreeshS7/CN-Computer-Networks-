import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 6002
format = 'utf-8'
client.connect((HOST,PORT))

while True:
    cal = input('Enter Expression : ')
    client.send(bytes(cal,format))
    data = client.recv(1024).decode()
    print('[RECEIVED ] Result: ',data)

client.close()
