from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture('/dev/video0')
ret, frame = cap.read()


model = YOLO('yolov8n.pt')
results = model(frame)

print(results)
