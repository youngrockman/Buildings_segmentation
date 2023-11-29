import os
import numpy as np
from PIL import Image

# Пути к папкам
output_folder = r'C:\pythonProject1test\rgb-footprint-extract\output_masks'

# Списки для хранения результатов
pixel_accuracy_scores = []

# Проход по всем маскам
for mask_name in os.listdir(output_folder):
    # Полный путь к маске
    mask_path = os.path.join(output_folder, mask_name)

    # Пропускаем файлы, не являющиеся изображениями (например, .DS_Store на macOS)
    if not mask_path.endswith(('.png', '.jpg', '.jpeg')):
        continue

    # Загрузка истинной маски
    true_mask_path = mask_path.replace("_predicted_mask", "_true_mask")
    true_mask = np.array(Image.open(true_mask_path))

    # Загрузка предсказанной маски
    predicted_mask = np.array(Image.open(mask_path))

    # Подсчет точности пикселей
    pixel_accuracy = np.sum(true_mask == predicted_mask) / np.prod(true_mask.shape)
    pixel_accuracy_scores.append(pixel_accuracy)

# Среднее значение точности пикселей
average_pixel_accuracy = np.mean(pixel_accuracy_scores)

# Вывод результата
print(f"Average Pixel Accuracy: {average_pixel_accuracy}")
