import pathsHandlers

###################################################
###################################################
#GET requests
def getPaths(path , headers):
    resp = ""
    if path.startswith("/echo"):
        resp = pathsHandlers.echoHandlerGet(path , headers)
    elif path.startswith("/files"):
        resp = pathsHandlers.fileHandlerGet(path)
    elif path.startswith("/user-agent"):
        resp = pathsHandlers.uagentHandlerGet(headers)
    elif path == '/':
        resp ="HTTP/1.1 200 OK\r\n\r\n"
    else:
        resp = "HTTP/1.1 404 Not Found\r\n\r\n"
    return resp



###################################################
###################################################
#POST requests
def postPaths(path , body):
    resp = ""
    if path.startswith("/files"):
        resp = pathsHandlers.fileHandlerPost(path , body)
    return resp