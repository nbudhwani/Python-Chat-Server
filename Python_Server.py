from socket import *
import datetime
import sys

TCP_IP = '192.168.0.28'	 #LAN 
TCP_PORT = 5021
s = socket(AF_INET, SOCK_STREAM) #Rules defining how socket act and play
s.bind((TCP_IP, TCP_PORT))	 #Binds socket to host and port		 
s.listen(1)  	  		 #Queue up to 1 request before refusing
conn, addr = s.accept()
print ('Connected with', addr)

dataRequest = ('What is the current date and time?'.encode(encoding='utf_8'))
while True:
	data = conn.recv(1024)	#Receive up to 1024 bytes of data using conn
	print ("Received:", repr(data.decode()))
	if data == dataRequest:	#If data received is the valid request, then
		dateAndTime = datetime.datetime.now()	#Display date and time in desired format
		day = "%02d" % dateAndTime.day
		month = "%02d" % dateAndTime.month
		year = "%02d" % dateAndTime.year
		hour = "%02d" % dateAndTime.hour
		minute = "%02d" % dateAndTime.minute
		second = "%02d" % dateAndTime.second
		reply = "Current Date and Time - " + day + "/" + month + "/" + year + " " + hour + ":" + minute + ":" + second
		conn.sendall(reply.encode(encoding='utf_8')) 
		print ('Listening for another connection...')
		conn, addr = s.accept()	#Keep listening for next connection
		print ('Connected with', addr)
		continue
	reply = "This is an invalid request. The valid request is 'What is the current date and time?'"	
	conn.sendall(reply.encode(encoding='utf_8'))  #sendall used so code can be easily modified to suit multiple clients at once

conn.close()





