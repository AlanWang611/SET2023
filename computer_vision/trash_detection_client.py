import cv2, shutil

def capture_image():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Capture a frame
    ret, frame = cap.read()

    if ret:
        # Save the captured frame as an image
        cv2.imwrite("frame.jpg", frame)
        # Send frame to trash_detection.py
        shutil.copy("frame.jpg", "trash_detection.pg")
    else:
        print("Error: Unable to capture image.")

    # Release the camera
    cap.release()

robot_on = True
while robot_on: 
  capture_image()