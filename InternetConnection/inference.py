# from ftplib import FTP
# ftp=FTP()
# ftp.connect("170.24.5.30",8869)
# print(ftp.getwelcome())

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data.decode('utf-8'))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'POST request received')

if __name__ == '__main__':
    server_address = ('', 8869)
    httpd = HTTPServer(server_address, MyRequestHandler)
    httpd.serve_forever()
