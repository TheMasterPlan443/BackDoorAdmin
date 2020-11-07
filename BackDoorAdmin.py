import os
import socket

# Create the socket
s = socket.socket()

# store info in variables to use later
host = socket.gethostname()
port = 8080

# Bind socket to address
s.bind(tuple((host, port)))
print("\nServer Is Running ", host, "\n", "Waiting For The Vitctim's Connection")

# listener
s.listen(1)
conn, addr = s.accept()
print("\n", addr, "Connection To Victim Is Successful : ")

""" TODO
#Command Control

#Taking Actions
"""
