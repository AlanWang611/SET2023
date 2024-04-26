from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from pathlib import Path


class HTTPRequestHandler(BaseHTTPRequestHandler):

    # POST method handler
    def do_GET(self):
        directory = '../computer_vision/images/'  # Adjust the path to your image directory

        try:
            # Get all image files in the directory
            files = list(Path(directory).glob('*'))
            # Filter files to only get those that are valid images
            image_files = [file for file in files if file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']]
            print(image_files)

            # Find the oldest file based on creation time
            oldest_file = max(image_files, key=os.path.getctime, default=None)

            if oldest_file is None:
                self.send_error(404, "No image files found.")
                return

            print(oldest_file)

            # Open the oldest image file and send it
            with open(oldest_file, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')  # Change if using different image types
                self.end_headers()
                self.wfile.write(file.read())
        except Exception as e:
            self.send_error(500, f"Server Error: {e}")


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server starting on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
