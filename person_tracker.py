import cv2
from ultralytics import YOLO
import numpy as np


model = YOLO('yolov8n.pt')


video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)


frame_id = 0
trackers = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_id % 30 == 0:  # Effectuer la détection toutes les 30 images
        results = model(frame)
        trackers = []

        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            scores = result.boxes.conf.cpu().numpy()
            classes = result.boxes.cls.cpu().numpy()

            for i in range(len(boxes)):
                x1, y1, x2, y2 = map(int, boxes[i])
                cls = int(classes[i])
                score = float(scores[i])

                if cls == 0 and score > 0.5:
                    trackers.append((x1, y1, x2, y2))
    
    for (x1, y1, x2, y2) in trackers:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, 'person', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    
    cv2.imshow('Person Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_id += 1

cap.release()
cv2.destroyAllWindows()
