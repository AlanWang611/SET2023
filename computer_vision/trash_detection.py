import ultralytics
from ultralytics import YOLO

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def predict_image(image_path):
    model = YOLO('best_trash.pt')
    # model.predict(image_path, save=True, imgsz=1280, conf=0.25, show_labels=True, show_conf=True, iou=0.5,
    #               line_width=3)
    result = model(image_path, imgsz=1280, conf=0.15, show_labels=True, show_conf=True, iou=0.5, line_width=3)
    # result boxes: all coords: x, y, width, height
    result_boxes = result[0].boxes.xywh.cpu().detach().numpy()
    return result_boxes


# Define the HTTP request handler class

saved_ndarray = None


class HTTPRequestHandler(BaseHTTPRequestHandler):

    # POST method handler
    def do_POST(self):
        global saved_ndarray

        # get length of data
        content_length = int(self.headers['Content-Length'])

        # read
        post_data = self.rfile.read(content_length)

        image_filename = 'litter.jpg'

        with open(image_filename, 'wb') as f:
            f.write(post_data)

        saved_ndarray = predict_image(image_filename)

        processed_result = predict_image(image_filename)

        # Convert the processed result to JSON format
        response_content = json.dumps(processed_result)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Send the processed result as the response body
        self.wfile.write(response_content.encode('utf-8'))


# server address
server_address = ('', 8000)

httpd = HTTPServer(server_address, HTTPRequestHandler)

# start
print('start server')
httpd.serve_forever()
