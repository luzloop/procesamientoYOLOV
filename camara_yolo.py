from ultralytics import YOLO
import cv2

# Cargar el modelo entrenado
model = YOLO('/Users/luzmariaescalona/Documents/procesamientoYOLOV/runs/peluches_entrenamiento_final/weights/best.pt')

# Abrir cámara
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo acceder a la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realiza la predicción directamente sobre el frame
    results = model.predict(source=frame, conf=0.3, device='cpu')

    # Mostrar resultados
    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("Detección de Peluches, Labubus y Capibaras", annotated_frame)

    # Salir con la tecla ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()