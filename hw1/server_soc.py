from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 5000))                                                      # ip and port number we know 5000 is not occupied

s.listen()                                                                       # enable server
print("Server listening...")


(conn, addr) = s.accept() # returns new socket and addr. for client          (new socket, add. of client)
print("1")

 while True: # forever                                                          loop
        data = conn.recv(1024) # receive data from client                     (buffer size)
        if not data: break # stop if client stopped
        conn.send(data+b'*') # return sent data plus an "*"                    nothing meaningful actually
 conn.close() # close the connection
