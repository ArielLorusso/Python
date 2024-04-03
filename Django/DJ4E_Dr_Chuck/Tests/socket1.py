import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make soket
mysock.connect(('data.pr4e.org', 80))     # connect port 80 to my course
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() # request +two enter
mysock.send (cmd)                         # send request

while True:                         # Blocking line
    data = mysock.recv(512)         # store 512 caractersdata
    if len(data) < 1:#              # END ? 
       break 
    print(data.decode(), end='')    # decode (http UTF-8 -> Python unicode )
    
mysock.close()                      # close our end
" Unicode uses a fixed character set," 
"while UTF-8 uses variable length."
"This means that UTF-8 can represent more than one character at a time , while Unicode just 1 "
