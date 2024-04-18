import ultralytics
from ultralytics import YOLO
from PIL import Image

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def predict_image(image_path):
    model = YOLO('best_trash.pt')
    # model.predict(image_path, save=True, imgsz=1280, conf=0.25, show_labels=True, show_conf=True, iou=0.5,
    #               line_width=3)
    im = Image.open(image_path).convert('RGB')
    result = model(im, imgsz=1280, conf=0.15, show_labels=True, show_conf=True, iou=0.5, line_width=3)
    print(result[0].tojson())
    # result boxes: all coords: x, y, width, height
    result_boxes = result[0].boxes.xywh.cpu().detach().numpy()
    return result_boxes



saved_ndarray = None


class HTTPRequestHandler(BaseHTTPRequestHandler):

    # POST method handler
    def do_POST(self):
        global saved_ndarray

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        image_filename = 'litter.jpg'

        with open(image_filename, 'wb') as f:
            f.write(post_data)

        prediction = predict_image(image_filename)
        saved_ndarray = prediction
        processed_result = prediction

        # response_content = json.dumps(processed_result)
        print(processed_result)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # self.wfile.write(response_content.encode('utf-8'))


# server address
server_address = ('', 8000)

httpd = HTTPServer(server_address, HTTPRequestHandler)

# start
print('start server')
httpd.serve_forever()
