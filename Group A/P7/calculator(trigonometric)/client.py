import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 6003
format = 'utf-8'

client.connect((HOST,PORT))

greetings = client.recv(1024).decode()
print(greetings)

while True:
    calc = input('[ENTER TRIGONOMETRIC EXPRESSION] : ')
    client.send(bytes(calc,format))
    if calc == 'exit':
        break
    ans = client.recv(1024).decode()
    print(f'[RECEIVED] : {ans}')

client.close()
