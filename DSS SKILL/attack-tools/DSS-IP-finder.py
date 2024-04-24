import socket

print("_"*80, "\nIP FINDER\n")

print("-"*80)
url = input("enter URL to find IP:")
print("-"*80)

ip = socket.gethostbyname(url)

print(ip)
