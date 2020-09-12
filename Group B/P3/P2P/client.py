
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST='localhost'
PORT=6002
format = 'utf-8'
client.connect((HOST,PORT))

prompt = client.recv(1024).decode()

print(prompt)
print('[MESSENGER STARTED]')
while True:
    data = client.recv(1024*1024).decode()
    if data == 'exit':
        break
    print('[Received] => ',data)
    client.send(bytes(input('[Send Message] => '),format))

client.close()
