"""
    Date: 29th September 2025
    Author: Rosey
    Description: Real-time PPE detection using YOLOv8 and OpenCV.
    This script captures video from the webcam, processes each frame using a trained YOLOv8 model,
    and displays the results with bounding boxes around detected PPE items.
    STEPS:
        - Requirements: ultralytics, opencv-python
        - Installation: pip install ultralytics opencv-python
        - best.pt: I trained YOLOv8 model file for PPE detection.
        - Datasets were collected from roboflow and google images.
        - Classes: Hardhat, Safety Vest, Safety Glasses, Masks
        - Then I annotated the images using Roboflow.
        - Downloaded the dataset in YOLOv8 format.
        - Uploaded to google drive to edit the path .yaml file on text editor.
        - Uploaded the dataset to Google Colab and trained the model using the following command:
        - !yolo task=detect mode=train model=yolov8n.pt data=PPE.yaml epochs=100 imgsz=640 batch=16
        - Training: 100 epochs, batch size 16, image size 640x640
        - After training, I downloaded the best.pt file to use in this script.

    STATUS: JOB COMPLETED!
"""

import cv2
from ultralytics import YOLO

# Load your trained YOLOv8n model
model = YOLO("best.pt")   # replace with the actual path if different

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO inference
    results = model(frame, stream=True)

    # Loop over results and draw bounding boxes
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Confidence score
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"

            # Draw rectangle + label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show video
    cv2.imshow("PPE Detection ", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
