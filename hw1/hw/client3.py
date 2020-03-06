import Pyro4

num = input("Please insert a number ").strip()
coder_creator = Pyro4.Proxy("PYRONAME:example.code")
print(coder_creator.func(num))
