import Pyro4

uri = input("Enter the URI of the server: ")
server = Pyro4.Proxy(uri)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = server.concatenate(s1, s2)
print("Concatenated string:", result)
