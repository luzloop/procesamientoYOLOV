from ultralytics import YOLO

# Carga el modelo base de YOLOv8
model = YOLO('yolov8n.pt')

# Entrenamiento usando tu dataset
model.train(
    data='datasets/peluches.v3i.yolov7pytorch/data.yaml',
    epochs=40,           # puedes aumentar si quieres mejor precisión
    imgsz=640,
    batch=4,
    name='peluches_entrenamiento_final',
    project='runs',
    exist_ok=True
)