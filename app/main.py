import socket
import threading
import handleReq
HOST = "localhost"
PORT = 4221
def main():
    #Server is ready to recieve request (maybe alot of concurrent requests at the same time)
    #
    #When a request is recieved it is given a thread to be handled this way the server is able to recieve 
    #and handle multiple concurrent requests at the same time
    server_socket = socket.create_server((HOST, PORT), reuse_port=True) 
    with server_socket:
        server_socket.listen() 
        while True:
            conn , address= server_socket.accept()
            req = threading.Thread(target = handleReq.handleReq , args=(conn,address))
            req.start()
    



if __name__ == "__main__":
    main()

