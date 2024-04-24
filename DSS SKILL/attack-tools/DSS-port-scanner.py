import socket
import sys
from datetime import datetime

print("_"*80, "\nPORT SCANNER\n")

RemoteSv = input("enter ip to scan ports  : ")
RemoteSvIp = socket.gethostbyname(RemoteSv)

print("-"*80)
print("don't press any key. scaning this IP:", RemoteSvIp, "         WAIT...")
print("-"*80)

T1 = datetime.now()

try:
    for port in range(1,65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        answer = sock.connect_ex((RemoteSvIp, port))
        T2 = datetime.now()
        T3 = T2 - T1
        if answer == 0:
            print("port {} :   open".format(port), "           ", T3, "    ", datetime.now())
        else:
            print("port {} :   close".format(port), "           ", T3, "    ", datetime.now())
        sock.close()
        print("."*80)

except KeyboardInterrupt:
    print("you pressed a keyboard key")
    sys.exit()
except socket.gaierror:
    print("can't connect to host")
    sys.exit()
except socket.error:
    print("server is not connected")
    sys.exit()

T4 = datetime.now()
T5 = T4 - T1
