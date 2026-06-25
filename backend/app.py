# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile! \n")

if __name__ == "__main__":
    # Serve on all interfaces (0.0.0.0) inside the container
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print("Hello from Effective Mobile!")
    server.serve_forever()