from ultralytics import YOLO
from PIL import Image
from http.server import BaseHTTPRequestHandler, HTTPServer
import io
import cv2
import time
import requests


image_count = 0
model = YOLO('best_trash.pt')

def predict_image(image_path):

    # model.predict(image_path, save=True, imgsz=1280, conf=0.25, show_labels=True, show_conf=True, iou=0.5,
    #               line_width=3)

    #plot stuff onto image
    im = cv2.imread(image_path)
    result = model(im, imgsz=1280, conf=0.15, show_labels=True, show_conf=True, iou=0.5, line_width=3)
    annotated_frame = result[0].plot()
    # cv2.imshow('Result', annotated_frame)
    # if cv2.waitKey(1) & 0xFF==ord("q"):
    #     return
    # cv2.destroyAllWindows()
    # cv2.waitKey(0)


    # result boxes: all coords: x1, y1, x2, y2
    # result_boxes = result[0].boxes.xyxy.cpu().detach().numpy()
    return result[0].tojson()


class HTTPRequestHandler(BaseHTTPRequestHandler):

    # POST method handler
    def do_POST(self):
        print("Got post")
        global image_count
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        image_filename = 'images/' + str(image_count) + '.jpg'
        image_count += 1
        with open(image_filename, 'wb') as f:
            f.write(post_data)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        prediction = predict_image(image_filename)
        print(prediction)
        self.wfile.write(prediction.encode('utf-8'))


def main():
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('start server')
    httpd.serve_forever()


if __name__ == "__main__":
    main()
