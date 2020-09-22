import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST = 'localhost'
PORT = 6000

soc = (HOST,PORT)
msg = b'Hello Server this is Client'
client.sendto(msg,soc)
file_name,addr = client.recvfrom(50*1024)
file_name = file_name.decode()
print('[RECEIVING FILE] : ',file_name)

dot = file_name.index('.')
extension = file_name[dot:]
file = file_name.replace(extension,'')
f_name = file+'_rec'+extension

file = open(f_name,'wb')
content,addr = client.recvfrom(50*4048)
file.write(content)
file.close()
print('[FILE RECEIVED SUCCESSFULLY] : Saved in current directory with name ,',f_name)
