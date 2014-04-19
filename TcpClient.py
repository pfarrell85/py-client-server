#!/usr/bin/env python

# Written by: Patrick Farrell
# 
# Basic TCP Client program that will connect to our TCP Server application

import sys
import socket
import struct
import string
import ctypes
import random
import time
import math

import signal

class TcpClient():

	
	def __init__(self):

		self.HOST = ''    # The remote host
		self.PORT = 50007  # The same port as used by the server
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		self.VERSION = 1
		self.listen_stop = False
		signal.signal(signal.SIGINT, self.signal_handler)
	
	def connect(self):	
		self.s.connect((self.HOST, self.PORT))

		#Send an initial message to the server when we connect
		self.s.send("This is a test message\n")

		#Sit in a loop and wait for messages from the server
		while self.listen_stop == False:
			try:
				data = self.s.recv(1024)

				if len(data) > 0:
					#print 'Received', repr(data)
					print 'Receive data len = %d' % len(data)

					try:
						print "ToDo: Decode message"
						print data
					except:
						print "Couldn't decode message header!"
			except:
				pass

	def closeClient(self):
		self.listen_stop = True
		self.s.close()

	def signal_handler(self, signal, frame):
		print 'Exiting Program'
		self.closeClient()
		sys.exit(0)

if __name__ == '__main__':

	client = TcpClient()
	client.connect()

	