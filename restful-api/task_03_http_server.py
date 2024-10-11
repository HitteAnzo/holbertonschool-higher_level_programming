#!/usr/bin/python3
"""
Simple HTTP server using http.server to handle GET requests.
This server responds to four endpoints:
- '/' : Returns a simple text message.
- '/data': Returns a JSON response with sample data.
- '/info': Returns a JSON response with version info.
- '/status': Returns a text response indicating server status.
"""


import http.server
import json

PORT = 8000
Handler = http.server.BaseHTTPRequestHandler


class Server(Handler):
    """
    Custom HTTP server handler to manage different GET endpoints.
    
    Handles the following routes:
    - "/" : Returns a plain text message.
    - "/data" : Returns a JSON object with sample user data.
    - "/info" : Returns a JSON object with version information.
    - "/status" : Returns a simple text response indicating server status.
    """


    def do_GET(self):
        """
        Handle GET requests based on the path.
        
        Returns:
            HTTP response with a status code, headers, and body content based on the endpoint.
        
        Raises:
            404 Not Found for unknown endpoints.
        """
        if self.path == '/':
            # Response for the root endpoint
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), Server) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
