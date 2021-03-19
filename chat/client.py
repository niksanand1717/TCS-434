import socket
import threading
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--ip", dest="hostIP", help="Enter IP address of chat server")
values, arguments = parser.parse_args()
if not values.hostIP:
    parser.error("Enter the host IP address")

host = values.hostIP
port = 55555
nickname = input("Choose a Nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An Error Occurred")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()