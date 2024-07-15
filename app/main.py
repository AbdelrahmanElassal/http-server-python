import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
        server_socket.listen() 
        conn , adress = server_socket.accept()
        with conn:
            data = conn.recv(1024)
            conn.sendall(b'HTTP/1.1 200 OK\r\n\r\n')



if __name__ == "__main__":
    main()


# git add .
# git commit -m "pass the 2nd stage" # any msg
# git push origin master