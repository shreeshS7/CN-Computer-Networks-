import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 6006
format = 'utf-8'
client.connect((HOST,PORT))

code = client.recv(1024).decode()
print(code)
r = client.recv(512).decode()
print(r)
arr = code
r = int(r)

def detectError(arr, nr):
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])

        res = res + val*(10**i)

    return int(str(res), 2)

check = detectError(arr,r)
if check == 0:
    print('Successfully Received without error')
else:
    print(f'error detected at position {check}')
