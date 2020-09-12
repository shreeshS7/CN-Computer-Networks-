
import socket
import time
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 6002
format = 'utf-8'
client.connect((HOST,PORT))

print(client.recv(20).decode())

file_name = client.recv(50*1024).decode()
print('[RECEIVING FILE] : ',file_name)

dot = file_name.index('.')
extension = file_name[dot:]
file = file_name.replace(extension,'')
f_name = file+'_rec'+extension
time.sleep(2)
try:
    file = open(f_name,'w')
    content = client.recv(50*4048).decode()
    file.write(content)
    file.close()
    print('[FILE RECEIVED SUCCESSFULLY] : Saved in current directory with name ,',f_name)
except:
    print('[FILE NOT RECEIVED]')
    client.close()

client.close()
