from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 5000))

s.listen()
print("Server listening...")


while True: # forever
        (conn, addr) = s.accept() # returns new socket and addr. clien
        data = conn.recv(1024) # receive data from client
        if not data: break # stop if client stopped
        conn.send(data+b'*') # return sent data plus an "*"
conn.close() # close the connection
