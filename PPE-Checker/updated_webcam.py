"""
    Date: 30th September 2025
    Author: Rosey
    Description: Real-time PPE detection using YOLOv8 and OpenCV.
    This script captures video from the webcam, processes each frame using a trained YOLOv8 model,
    and displays the results with bounding boxes around detected PPE items.

    Hardware is ben tinkered into this with the help of:
      - Arduino uno
      - LEDs
      - Resistors

      The Green Led comes up when all PPE are been worn
      The Red LEDs comes up when no PPE is worn

      A certain confidence level has to be reached in order to do this.

    STATUS: JOB COMPLETED!
"""

import cv2
import serial
import time
from ultralytics import YOLO

# Load your trained YOLOv8n model
model = YOLO("best.pt")   # replace with the actual path if different

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

arduino = serial.Serial("COM10", 9600)
time.sleep(2)

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
            
            # Track which PPE items are present
            PPE_worn = {"Hardhat": False, "Safety Vest": False, "Safety Glasses": False, "Masks": False}

            for r in results:
                for box in r.boxes:
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    if conf > 0.5:
                        class_name = model.names[cls]
                        if class_name in PPE_worn:
                            PPE_worn[class_name] = True

            # Green only if ALL PPE are True
            ppe_detected = all(PPE_worn.values())


            if PPE_worn:
                arduino.write(b'1')   # turn LED on
            else:
                arduino.write(b'0')   # turn LED off

    # Show video
    cv2.imshow("PPE Detection ", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
