from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 5000)) # connect to server (block until accepted)

print("Please insert a number and press enter")
num= input() 
s.send(bytes(str(num), 'utf8'))

data = s.recv(1024) # receive the response
print('Received', data) # print the result

s.close() # close the connection

