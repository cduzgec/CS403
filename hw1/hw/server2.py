from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 5000))

s.listen()
print("Server listening...")

def func(data):

	#Q(x) = a0 + a1x + a2x2 + a3x3 + a4x4

   p = 82774018375762036230659850750851711854039699313175216914470363560945323457727
   a0 = 26748908084769669758664722731140522800875206292361297608046702271758631669759
   a1 = 59489944712712493230446426050522902095714591665803937192613571374709152682872
   a2 = 71257019652372732006624209284281187993740077445682918560838974809666187201576
   a3 = 55315635592811832356973556884353215645720087042315880077665613542569819620485
   a4 = 20411929856341763513465955098957309007252776763418101366798367886225234827183

   x0= a0%p
   x1= a1%p
   x2=a2%p
   x3=a3%p
   x4=a4%p
   d = data%p

   send_data= (x0 + (x1*d)%p + (x2*d*d)%p + (x3*d*d*d)%p + (x4*d*d*d*d)%p) %p
   
   return send_data

while True: # forever
        (conn, addr) = s.accept() # returns new socket and addr. clien
        data = conn.recv(1024) # receive data from client
        if not data: break # stop if client stopped
		# decode to unicode string
        strings = str(data, 'utf8')
        #get the num
        num = int(strings)
        x=func(num)
        conn.send(bytes(str(x), 'utf8')) # return sent data plus an "*"
conn.close() # close the connection
