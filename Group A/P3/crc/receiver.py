import socket
import random
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 8008

s.connect((HOST,PORT))
data = s.recv(14).decode()
print(data)


def crc(a,gene):
    code_word = a

    gen = gene
    #print(gen)

    dlen = len(code_word)

    dividend = code_word[0:len(gen)]
    x = len(gen)
    count = 0
    while count < len(gen):
        if dividend[0] == 0:
            divisor = [0] * len(divisor)
        else:
            divisor = gen
        res = [ dividend^ divisor for dividend,divisor in zip(dividend,divisor)]
        try:
            res.append(code_word[x])
        except:
            res = [ dividend^ divisor for dividend,divisor in zip(dividend,divisor)]
        res.remove(res[0])
        #print(x)
        #print(res)
        x = x+1
        dividend = res
        count += 1
    if res == [0,0,0]:
        print(res)
        print('Data Successfully received')
    else:
        print('Data discarded')


gene = []
while True:
        data = s.recv(1).decode()
        print(data)
        gene.append(int(data))
        if len(gene) == 4:
            break
print('Received Generator :',gene)
code = []
while True:
    try:
        data = s.recv(1).decode()
        print(data)
        s.send(bytes('Ack','utf-8'))
        code.append(int(data))
    except:
        break
print('Received Code_word :',code)

crc(code,gene)
