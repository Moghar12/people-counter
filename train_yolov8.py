from ultralytics import YOLO


model = YOLO('yolov8n.pt')


model.train(data='data_person/data.yaml', epochs=100, imgsz=640)
