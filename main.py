from ultralytics import YOLO
import cv2
import threading

# Load the YOLO model
model = YOLO('yolov8s.pt')

# Video path and capture
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video.")
    exit()

# Initialize variables
frame_skip = 6
frame_counter = 0
line_position = 200
people_inside = 0
entry_count = 0
exit_count = 0
tracked_objects = {}

# Process each frame
def process_frame(frame):
    global people_inside, entry_count, exit_count, tracked_objects
    
    results = model(frame)
    for result in results:
        boxes = result.boxes.xyxy.numpy()
        scores = result.boxes.conf.numpy()
        class_ids = result.boxes.cls.numpy()
        
        for i, class_id in enumerate(class_ids):
            label = model.names[int(class_id)]
            if label in ['person']:
                object_id = i  # Assume 'i' can be used as a unique identifier for the object
                x1, y1, x2, y2 = map(int, boxes[i][:4])
                conf = scores[i]

                if label in ['person']:
                    display_label = 'person'
                
                if object_id not in tracked_objects:
                    tracked_objects[object_id] = {"entered": False, "exited": False}

                # Draw the rectangle and label on the frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{display_label} {object_id + 1}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                # Check if the object crosses the line
                if y2 > line_position and not tracked_objects[object_id]["entered"]:
                    if y1 < line_position:
                        entry_count += 1
                        people_inside += 1
                        tracked_objects[object_id]["entered"] = True
                        tracked_objects[object_id]["exited"] = False
                    elif y1 > line_position and tracked_objects[object_id]["entered"] and not tracked_objects[object_id]["exited"]:
                        exit_count += 1
                        people_inside -= 1
                        tracked_objects[object_id]["exited"] = True

    # Draw the prediction border
    cv2.line(frame, (0, line_position), (frame.shape[1], line_position), (0, 0, 0), 2)
    cv2.putText(frame, '-Prediction Border-', (frame.shape[1] // 3, line_position - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    
    # Display status and counts
    cv2.putText(frame, f'Status: Tracking', (10, frame.shape[0] - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f'Entrer: {entry_count}', (10, frame.shape[0] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f'Exit: {exit_count}', (10, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f'Total people inside: [{people_inside}]', (frame.shape[1] - 250, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    return frame

# Main loop
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    
    if frame_counter % frame_skip == 0:
        thread = threading.Thread(target=process_frame, args=(frame,))
        thread.start()
        thread.join()
        cv2.imshow('Object Detection', frame)
    
    frame_counter += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()