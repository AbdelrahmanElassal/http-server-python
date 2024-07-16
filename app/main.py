import socket
import threading
import os
import sys

def fileHandler(path):
    directory = sys.argv[2]
    [x,y,filename] = path.split('/')
    try:
        with open(directory+filename , r) as f:
            filecontent = f.read()
            return "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: " + str(len(filecontent)) + "\r\n\r\n" + filecontent
    except FileNotFoundError:
        return "HTTP/1.1 404 Not Found\r\n\r\n"
def echoHandler(path):
    [f,r,bod] = path.split('/')
    resp = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: " + str(len(bod)) + "\r\n\r\n" + bod
    return resp

def yagentHandler(headers):
    [q , bod] = headers[1].split(": ")
    resp = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: " + str(len(bod)) + "\r\n\r\n" + bod 
    return resp

def parseReq(reqmess): #req -> "GET /index.html HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\nAccept: */*\r\n\r\n"
    [rq_line , Rest] = reqmess.split("\r\n" , 1)
    [method , path , ex] = rq_line.split(" ")
    [header , body] = Rest.split("\r\n\r\n")
    Headers = header.split("\r\n")
    return [path , Headers]
    
    
def handleReq(conn , address):
    with conn:
        data = conn.recv(1024)
        [path , headers] = parseReq(data.decode('ascii'))
        resp = ""
        if path.startswith("/echo"):
            resp = echoHandler(path)
        elif path.startswith("/files"):
            resp = fileHandler(path)
        elif path.startswith("/user-agent"):
            resp = yagentHandler(headers)
        elif path == '/':
            resp ="HTTP/1.1 200 OK\r\n\r\n"
        else:
            resp = "HTTP/1.1 404 Not Found\r\n\r\n"
        conn.sendall(resp.encode())


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True) 
    with server_socket:
        server_socket.listen() 
        while True:
            conn , address= server_socket.accept()
            req = threading.Thread(target = handleReq , args=(conn,address))
            req.start()
    



if __name__ == "__main__":
    main()

