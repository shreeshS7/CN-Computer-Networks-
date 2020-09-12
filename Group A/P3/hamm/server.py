import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 6006
format = 'utf-8'
server.bind((HOST,PORT))
server.listen()
print('[LISTENING]...')
conn,addr = server.accept()
print(f'[CONNECTION ESTABLISHED WITH {addr}]')


def getbits():
    databit = [str(x) for x in [1,0,1,1,0,0,1]]
    return databit

def check(m):
    r = 1
    while (2**r < m+r+1):
        r +=1
    return r

def hammcode(data,r):

    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])

        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr


databits = getbits()
m = len(databits)
r = check(m)
print(r)
code = hammcode(databits,r)
print(code)
hcode = calcParityBits(code,r)
print(hcode)
conn.send(bytes(hcode,format))
conn.send(bytes(str(r),format))

conn.close()
server.close()
