
import os
import numpy as np
from PIL import Image

# Пути к папкам
images_folder = r'C:\pythonProject1test\rgb-footprint-extract\ready images'
output_folder = r'C:\pythonProject1test\rgb-footprint-extract\output_masks'

# Создание папки для сохранения масок, если ее нет
os.makedirs(output_folder, exist_ok=True)

# Проход по всем изображениям в папке
for image_name in os.listdir(images_folder):
    # Полный путь к изображению
    image_path = os.path.join(images_folder, image_name)

    # Открываем изображение с использованием PIL
    img = Image.open(image_path)

    # Получаем размеры изображения
    width, height = img.size

    # Создание истинной маски (предположим, что у вас есть заранее подготовленные маски для каждого изображения)
    true_mask_path = os.path.join(output_folder, image_name.replace(".jpg", "_true_mask.png"))
    # Пример: создание случайной истинной маски
    true_mask = np.random.randint(2, size=(224, 224), dtype=np.uint8) * 255
    Image.fromarray(true_mask).save(true_mask_path)

    # Определение маски (здесь можно использовать свою модель для предсказания маски)
    predicted_mask_array = np.random.randint(2, size=(min(height, 224), min(width, 224)), dtype=bool)

    # Преобразование маски в бинарную маску, где белый цвет - здания, черный - фон
    predicted_mask = predicted_mask_array.astype(np.uint8) * 255

    # Сохранение предсказанной маски
    predicted_mask_path = os.path.join(output_folder, image_name.replace(".jpg", "_predicted_mask.png"))
    Image.fromarray(predicted_mask).save(predicted_mask_path)