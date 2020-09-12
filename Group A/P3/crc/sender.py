import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 8008

s.bind((HOST,PORT))
s.listen()
client, addr = s.accept()
print(client,'connected with',addr)
client.send(bytes('Welcome client','utf-8'))

client.settimeout(0.3)
def crc():


    dlen = len(data_word)
    data_word.extend([0,0,0])

    dividend = data_word[0:len(gen)]
    x = len(gen)
    count = 0
    while count < len(gen):
        if dividend[0] == 0:
            divisor = [0] * len(divisor)
        else:
            divisor = gen
        res = [ dividend^ divisor for dividend,divisor in zip(dividend,divisor)]
        try:
            res.append(data_word[x])
        except:
            res = [ dividend^ divisor for dividend,divisor in zip(dividend,divisor)]
        res.remove(res[0])
        #print(x)
        #print(res)
        x = x+1
        dividend = res
        count += 1

    code_word = data_word[0:dlen]
    code_word.extend(res)
    #print('Code Word: ',code_word)
    return code_word

data_word = [int(item) for item in input('Enter data word with spaces').split()]
print(data_word)
gen = [int(item) for item in input('Enter Generator').split()]
print(gen)
for item in gen:
    client.send(bytes(str(item),'utf-8'))
code_word = crc()
print(code_word)


for item in code_word:
    client.send(bytes(str(item),'utf-8'))
    try:
        ack = client.recv(8).decode()
        print('Sent Successfully')
    except socket.timeout:
        print('Nack')
    time.sleep(0.3)
