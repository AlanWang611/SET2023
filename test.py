import cv2

def main():
  vid = cv2.VideoCapture(0)

  while True:
    ret, frame = vid.read()
    if not ret:
      print("Failed to capture frame")
      break
    cv2.imwrite("frame.jpg", frame)
