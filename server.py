import json
import socket                   # Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = ""   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    address = addr[0]

    filename='test.py' #In the same folder or path is this file running must the file you want to tranfser to be
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()

    with open('ips.json', 'r') as f:
        ips = json.load(f)  # import ip list

    
    find = False
    for i in  ips:
        if i == address:
            print('your address already here')
            find = True

    if find == False:
        ips.append(address) # append yout ip address

    with open('ips.json', 'w', encoding='utf-8') as make_file:
        json.dump(ips, make_file, indent="\t") 

