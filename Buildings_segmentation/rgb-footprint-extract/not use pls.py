from PIL import Image
import os
import numpy as np

# Пути к папкам
images_folder = 'C:\\pythonProject1test\\rgb-footprint-extract\\ready images'

# Проход по всем изображениям в папке
for image_name in os.listdir(images_folder):
    # Полный путь к изображению
    image_path = os.path.join(images_folder, image_name)

    # Открываем изображение с использованием PIL
    img = Image.open(image_path)

    # Получаем размеры изображения
    width, height = img.size
    print(f"Image: {image_name}, Width: {width}, Height: {height}")

    # Определение маски (здесь можно использовать свою модель для предсказания маски)
    mask_array = np.ones((height, width), dtype=np.uint8)  # Пример: создаем белую маску

    # Получение размеров массива маски
    mask_height, mask_width = mask_array.shape
    print(f"Mask: Width: {mask_width}, Height: {mask_height}")
