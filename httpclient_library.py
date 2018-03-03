#Author :	1) Maniar Meet (40039203)
#			2) Athalye Shriyans (40037637)
import socket
import argparse
import urllib.parse
import json

def writeToFile(response, pathName):
    if pathName:
        file = open(pathName, 'w')
        file.write(response)
        print("Output has been saved to file.")
    else:
        print(response)
    pass

def redirect(response):
    resp=response
    head=resp.split("\r\n")
    check=int(head[0].split(" ")[1])
    if (check > 299 and check < 400):
        for headers in head :
            if("Location: " in headers):
                location=head.split(":")[1]
        if(location):
            print("URL redirecting",location)
            return location
        else:
            print("Cannot redirect")


def http_post(s, headers, data, domain, path, method, verbose, o):

   
    data_str = str(data).encode("utf-8")

   
    formattedHeaders = "\r\n".join(headers)

   
    content_header = "Content-Length: " + str(len(data_str))

    request_string = "POST /post HTTP/1.1\r\nHost: %s\r\n%s\r\n%s\r\n\r\n%s" % (domain, formattedHeaders, content_header, data)
    return request_string

def http_get(argm):
    parsed_uri = urllib.parse.urlparse(argm.url)
    domain = 'www.{uri.netloc}'.format(uri=parsed_uri)
    path = '{uri.path}?{uri.query}'.format(uri=parsed_uri)
    method = argm.gp.upper()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((domain, 8007))

    if method == 'GET':
        request_string = '%s %s HTTP/1.1\r\nHost: %s\r\nUser-Agent:Concordia-HTTP/1.1\r\nAuthors:Meet and Shriyans\r\n\r\n' % (
            method, path, domain)
        s.send(request_string.encode(encoding='utf-8'))
    else:
        filePath = argm.file
        if filePath:
            with open(filePath) as f:
                data = ""
                for line in f:
                    data += line
            request_string = http_post(s, argm.h, data, domain, path, method, argm.verbose,
                                             argm.o)
        else:
            request_string = http_post(s, argm.h, argm.data, domain, path, method, argm.verbose,
                               argm.o)
        s.send(request_string.encode(encoding='utf-8'))
    result = (s.recv(4096).decode('utf-8'))
    """location=redirect(result)
    if(location):
        http_get(location,argm.v,argm.h,path)
    else:
        response=argm.v(result,argm.v)
        writeToFile(response,path)"""
    if argm.verbose is False:
        (h, js) = result.split('\r\n\r\n')
        data = json.loads(js)
        print(data)
    else:
        print(result)
    if argm.o:
            writeToFile(result, argm.o)
    s.close()