###################################################
###################################################
#Extract info from Http Request to handle it and return a dictionary for the req content
def parseReq(reqmess): #req -> "GET /index.html HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\nAccept: */*\r\n\r\n"
    [rq_line , Rest] = reqmess.split("\r\n" , 1)
    [method , path , ex] = rq_line.split(" ")
    [header , body] = Rest.split("\r\n\r\n")
    Headers = header.split("\r\n")
    return {
        "req_line" : {
            "method":method,
            "path"  :path,
            "ex"    :ex
        },
        "headers"   :Headers,
        "body"     :body
    }
    