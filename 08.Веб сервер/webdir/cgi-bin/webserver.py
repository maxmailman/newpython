'''
Реализация веб-сервера на языке Python, способная запускать серверные
CGI-сценарии на языке Python; обслуживает файлы и сценарии в текущем
рабочем каталоге; сценарии на языке Python должны находиться в каталоге
webdir\cgi-bin или webdir\htbin;
'''
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webir = '.'
port = 80

os.chdir(webir)
srvaddr = ("", port)
srvrobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()