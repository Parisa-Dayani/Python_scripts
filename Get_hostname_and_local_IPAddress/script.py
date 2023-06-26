# Get Hostname and Local IP Address using Class
import socket

class CodesCracker:
    def FindHost(self):
        return socket.gethostname()
    def FindIP(self):
        hn = self.FindHost()
        ip = socket.gethostbyname(hn)
        return ip

obj = CodesCracker()
print("\nHostname or Device Name =", obj.FindHost())
print("Local IP Address =", obj.FindIP())



#Get Hostname and IP Address using Function
'''
import socket

def FindHost():
    #return socket.gethostname()

def FindIP():
    hn = FindHost()
    ip = socket.gethostbyname(hn)
    return ip

print("\nHostname =", FindHost())
print("IP Address =", FindIP())
'''
