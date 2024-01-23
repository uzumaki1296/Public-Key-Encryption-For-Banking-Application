# Public-key Encryption for Banking Application
This is an iterative secure banking application consisting of a bank server and multiple clients using Public-key encryption.

Server : 
    python3 server/sshserv.py 5063

Client : 
    python3 client/sshcli.py remote0x.cs.binghamton.edu 5063

Enter PEM pass phrase: password

Algorithm:

i) Server :
    Port number is provided as command line argument. Host of the current server is used and the socket 
    is wrapped with the ssl keyfile and certfile. Then the socket is binded and waits to accept the 
    connection. Once connected to a client, server waits to receive message. 
    
    - If message is "ls", then os.listdir() is used and result is sent back.
    - If message is "pwd", os.getcwd() is used and result is sent back. 
    - If message is "exit", then the server is closed.

ii) Client :
    Host and Port number are provided as command line argument. Socket is wrapped with the same ssl key 
    and certificate. Once connected to server, message is got from user and transmitted to server. Then 
    the returned message is displayed to user. If message is "exit", then the socket is closed. 

Reference : 

1. Server client : https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
2. SSL socket : https://gist.github.com/Oborichkin/d8d0c7823fd6db3abeb25f69352a5299
