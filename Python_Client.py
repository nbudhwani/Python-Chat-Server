from socket import *
import sys

#READ.ME: (1) save file and 'cd ..' to this path (2) type 'python3 Python_Client.py' on command line  

TCP_IP='172.16.76.129'
TCP_PORT = 5020
print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
responseForInvalidRequest = "This is an invalid request. The valid request is 'What is the current date and time?'"
encodedResponseForInvalidRequest = (responseForInvalidRequest.encode(encoding='utf_8'))
while True:
    message = input("Your request: ")
    s.send(message.encode(encoding='utf_8'))
    reply = s.recv(1024)
    print (repr(reply.decode()))

    substring = "Current".encode(encoding='utf_8')
    if reply != encodedResponseForInvalidRequest:  #If the request is valid
            s.close()                       #Then, close the connection
            sys.exit()                      #Terminate program
s.close()
