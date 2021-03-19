import socket
import threading
import re
import subprocess as sp

pattern = "(\d+)\.(\d+)\.(\d+)\.(\d+)"
ifconfig_result = str(sp.check_output(["ifconfig", "wlan0"]))
ipaddr = re.search(pattern, ifconfig_result)
# print(ipaddr.group(0))

host = str(ipaddr.group(0))
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(f"Server Started at {host}")

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        client.send('Connected to server........'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

receive()
