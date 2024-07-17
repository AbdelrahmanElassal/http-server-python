import sys
import gzip

DIRECTORY_ARGUMENT_INDEX = 2

###################################################
###################################################
# For POST requests

def fileHandlerPost(path , body):
    directory = sys.argv[DIRECTORY_ARGUMENT_INDEX]
    [x,y,filename] = path.split('/')
    with open(directory+filename , "w") as f:
        f.write(body)
    return "HTTP/1.1 201 Created\r\n\r\n"

###################################################
###################################################
# For GET requests

def fileHandlerGet(path):
    directory = sys.argv[DIRECTORY_ARGUMENT_INDEX]
    [x,y,filename] = path.split('/')
    try:
        with open(directory+filename , "r") as f:
            filecontent = f.read()
            return "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: " + str(len(filecontent)) + "\r\n\r\n" + filecontent
    except FileNotFoundError:
        return "HTTP/1.1 404 Not Found\r\n\r\n"



def echoHandlerGet(path , headers):
    [f,r,bod] = path.split('/')
    allencoding = ""
    resp = ""
    for el in headers:
        if el.startswith("Accept-Encoding"):
            allencoding = el.split(": ")[1]
            break
    encodlist = allencoding.split(", ")
    if "gzip" in encodlist: 
        compBod = gzip.compress(bod.encode('ascii'))
        resp = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Encoding: gzip\r\nContent-Length: " + str(len(compBod)).encode('ascii') + b"\r\n\r\n" + compBod
    else:
        resp = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: " + str(len(bod)) + "\r\n\r\n" + bod
    return resp



def uagentHandlerGet(headers):
    [q , bod] = headers[1].split(": ")
    resp = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: " + str(len(bod)) + "\r\n\r\n" + bod 
    return resp
