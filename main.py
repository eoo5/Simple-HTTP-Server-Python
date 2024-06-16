from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "localhost"  # or "" to bind to all interfaces
PORT = 8000  # replace with the port you want to use

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1> HELLO WORLD!</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes(f'{{"time":"{date}"}}', "utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print(f"Starting server on {HOST}:{PORT}")
server.serve_forever()
