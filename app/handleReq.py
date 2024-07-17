import parseReq
import Paths
BUFFER = 1024
###################################################
###################################################
#Once the connection is opened request is recieved parsed and handled 
#by the suitable function according to the method and the path

def handleReq(conn , address):
    with conn:
        data = conn.recv(BUFFER)
        req = parseReq.parseReq(data.decode('ascii'))
        path = req["req_line"]["path"]
        headers = req["headers"]
        method = req["req_line"]["method"]
        resp = ""
        if method.startswith("GET"):
            resp = Paths.getPaths(path , headers)
        elif method.startswith("POST"):
            resp = Paths.postPaths(path , req["body"])
        
        if isinstance(resp, str):
            resp = resp.encode()
        conn.sendall(resp)
