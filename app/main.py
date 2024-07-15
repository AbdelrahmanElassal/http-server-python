import socket

def handleReq(reqmess):
    
    Req_line , Rest = reqmess.split("/r/n" , 1)
    Headers , Body = Rest.split("/r/n/r/n" , 1)
    method , path , version = Req_line.split()

    headersdic = []
    for el in Headers.split("/r/n"):
        if el:
            key, value = el.split(': ', 1)
            headersdic[key] = value
    
    return (method , path)


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True) 
    server_socket.listen() 
    conn = server_socket.accept()
    data = conn.recv(1024)
    method , path = handleReq(data.decode('ascii'))
    resp = ""
    if path == "/index.html" :
        resp = "HTTP/1.1 404 Not Found\r\n\r\n"
    else:
        resp = "HTTP/1.1 200 OK\r\n\r\n"
    conn.sendall(resp.encode())


    



if __name__ == "__main__":
    main()


# git add .
# git commit -m "pass the 2nd stage" # any msg
# git push origin master