import Pyro4
import random


@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {arg1}. Today’s lucky number is: {arg2}.".format(arg1=name, arg2=random.randint(0, 10 ** 6))


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(GreetingMaker)
ns.register("example.greeting", uri)

print('ready')
daemon.requestLoop()
