import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# print(socket.gethostname())
# while True:
msg = s.recv(1024) #how big the chucks of data we want to receive of a time
print(msg.decode("utf-8"))