import socket

host = '127.0.0.1'
port = 55555

receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver.connect((host, port))

while True:
    receiver.send("OTP RECV".encode('utf-8'))
    otp = receiver.recv(6)
    print("OTP : ", otp.decode('utf-8'))
    resend = input("[*] Press 'R' to resend the OTP or press ENTER to continue")
    if resend == ord('r'):
        continue
