
# https://docs.python.org/3/howto/sockets.html
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries


from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(('localhost',9000))
        serversocket.listen(5) # Queue the incoming connections to 5 if bussy
        while(1):
            (clientsocket, address) = serversocket.accept() #receve

            rd = clientsocket.recv(5000).decode()  # decode
            pieces = rd.split(" ")
            if ( len(pieces) > 0 ):
                for word in pieces :
                    print(word)

            data = "HTTP/1.1 200 OK\r\n"        # generate response
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()
                                # main
print('Access http://localhost:9000') # ask user to connect
createServer()                        # start server