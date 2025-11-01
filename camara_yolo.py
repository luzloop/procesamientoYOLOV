from ultralytics import YOLO
import cv2

# Cargar el modelo entrenado
model = YOLO('/Users/luzmariaescalona/Documents/procesamientoYOLOV/runs/peluches_entrenamiento_final/weights/best.pt')

# Abrir cámara (0 = cámara integrada del Mac)
camara = cv2.VideoCapture(0)

while True:
    ret, frame = camara.read()
    if not ret:
        break

    # Realizar detección
    results = model(frame)

    # Mostrar resultados en la ventana
    annotated_frame = results[0].plot()
    cv2.imshow("Detección de Peluches, Labubus y Capibaras", annotated_frame)

    # Presionar ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Liberar cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()