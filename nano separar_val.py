import os, random, shutil

# Directorios
train_dir = 'datasets/mi_dataset/images/train'
val_dir = 'datasets/mi_dataset/images/val'

# Crear carpeta de validación si no existe
os.makedirs(val_dir, exist_ok=True)

# Recorre todas las subcarpetas dentro de train
for carpeta in os.listdir(train_dir):
    subcarpeta = os.path.join(train_dir, carpeta)
    if not os.path.isdir(subcarpeta):
        continue
    
    # Crea la subcarpeta en val
    os.makedirs(os.path.join(val_dir, carpeta), exist_ok=True)

    # Lista de imágenes
    imagenes = [img for img in os.listdir(subcarpeta) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(imagenes)

    # Calcula el 20%
    n_val = max(1, int(len(imagenes) * 0.2))
    val_imgs = imagenes[:n_val]

    # Mueve las imágenes seleccionadas
    for img in val_imgs:
        origen = os.path.join(subcarpeta, img)
        destino = os.path.join(val_dir, carpeta, img)
        shutil.move(origen, destino)

print("✅ Se movió el 20% de las imágenes a la carpeta de validación.")