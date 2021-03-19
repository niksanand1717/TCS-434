import socket
import random
import threading
import time

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("Server Started at ", format(host))

def otpGenerator():
    otp = random.randint(100000, 999999)
    return otp

def receive():
    otpTries = 0
    while otpTries < 3:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        otp = str(otpGenerator())
        print(otp)

        message = client.recv(6).decode('ascii')
        if message == 'OTP RECV':
            client.send(str(otp))

        time.sleep(10)
                # print("try")
        # except:
        #     client.send("An Error Occurred".encode('ascii'))
        #     client.close()

        otpRecevied = client.recv(1000).decode('ascii')
        if otpRecevied == otp:
            client.send("OTP accepted".encode('ascii'))
        else:
            otp = otp.encode('ascii')
            client.send(otp)
            client.send("Enter the new otp sent".encode('ascii'))
        otpTries += 1
        print("last")


receive()