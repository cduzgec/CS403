import Pyro4

name = input("What is your name? ").strip()
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")
print(greeting_maker.get_fortune(name))

# saved as server.py
import Pyro4
import random

@Pyro4.expose
class GreetingMaker(object):
	def get_fortune(self, name):
		return "Hello, {arg1}. Today’s lucky number is: {arg2}." \	 4\.format(arg1=name,arg2=random.randint(0,10**6))


p = 82774018375762036230659850750851711854039699313175216914470363560945323457727
a0 = 26748908084769669758664722731140522800875206292361297608046702271758631669759
a1 = 59489944712712493230446426050522902095714591665803937192613571374709152682872
a2 = 71257019652372732006624209284281187993740077445682918560838974809666187201576
a3 = 55315635592811832356973556884353215645720087042315880077665613542569819620485
a4 = 20411929856341763513465955098957309007252776763418101366798367886225234827183

daemon = Pyro4.Daemon() 	# make a Pyro daemon
ns = Pyro4.locateNS() 	# find the name server
uri = daemon.register(GreetingMaker) 	# register the greeting maker as a Pyro object
ns.register("example.greeting", uri) 	# register the object with a name in the name server

print "Ready."
daemon.requestLoop()
