from http.server import HTTPServer, CGIHTTPRequestHandler
print("server has been started ")
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
