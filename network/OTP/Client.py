import socket

def sendOtp(otp):
    sender.send(otp)

host = '127.0.0.1'
port = 55555

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sender.connect((host, port))
    print("Connected to the server")
except:
    print("An error occourred")


while True:
    sender.send('OTP RECV'.encode('ascii'))
    otp = input("Enter OTP for verification: ")
    otp = otp.encode('ascii')
    sendOtp(otp)
    message = sender.recv(100)
    message = message.decode('ascii')
    if 'accepted' in message:
        print(message.encode('ascii'))
        break
    else:
        continue
