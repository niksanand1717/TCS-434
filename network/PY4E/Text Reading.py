import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('127.0.0.1', 8000))
cmd = 'GET http://127.0.0.1:8000/romeo-full.txt HTTP/0.6\r\n\r\n'.encode('utf-8')
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysocket.close()
