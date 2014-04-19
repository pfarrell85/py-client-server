
# TCP Server Program
# Written by: Patrick Farrell

import os
import sys
import socket

class TcpServer():

	def __init__(self):
		self.HOST = ''              # Symbolic name meaning the local host
		self.PORT = 50007           # Arbitrary non-privileged port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((self.HOST, self.PORT))

	def listen(self):

		print "Listening for data..."
		self.s.listen(1)

		conn, addr = self.s.accept()
		print 'Connected by', addr

		while 1:
			data = conn.recv(1024)
			if not data: break
			conn.send(data)
		conn.close()

if __name__ == '__main__':

	tcpserver = TcpServer();
	tcpserver.listen();