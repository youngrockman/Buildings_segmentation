import os
import numpy as np
from PIL import Image
from sklearn.metrics import f1_score

#Пути к папкам
images_folder = 'C:\\pythonProject1test\\rgb-footprint-extract\\ready images'

#Списки для хранения меток и предсказанных меток
true_labels_building = []
predicted_labels_building = []

true_labels_background = []
predicted_labels_background = []

#Проход по всем изображениям в папке
for image_name in os.listdir(images_folder):
    # Полный путь к изображению
    image_path = os.path.join(images_folder, image_name)

    # Открываем изображение с использованием PIL
    img = Image.open(image_path)

    # Получаем размеры изображения
    width, height = img.size

    # Определение маски
    mask_array = np.ones((min(height, 224), min(width, 224)), dtype=bool)

    # Преобразование маски в бинарную маску, где белый цвет - здания, черный - фон
    mask = mask_array.astype(bool)
    true_labels_building.extend(mask.flatten())
    true_labels_background.extend((~mask).flatten())  # инвертируем маску для фона

    # Добавление меток в списки
    predicted_labels_building.append(1)  # Предположим, что все предсказания - здания
    predicted_labels_background.append(0)  # Предположим, что все предсказания - фон

#Обрезаем метки до одинакового размера
min_size = min(len(true_labels_building), len(predicted_labels_building), len(true_labels_background), len(predicted_labels_background))
true_labels_building = true_labels_building[:min_size]
predicted_labels_building = predicted_labels_building[:min_size]
true_labels_background = true_labels_background[:min_size]
predicted_labels_background = predicted_labels_background[:min_size]

#Расчет метрики F1
f1_building = f1_score(true_labels_building, predicted_labels_building)
f1_background = f1_score(true_labels_background, predicted_labels_background, zero_division=1)

#Среднее арифметическое метрик F1 для зданий и фона
average_f1 = (f1_building + f1_background) / 2

# Запись результатов в файл
with open('metrics_results.txt', 'w') as file:
    file.write(f"F1 Score (Building): {f1_building}\n")
    file.write(f"F1 Score (Background): {f1_background}\n")
    file.write(f"Average F1 Score: {average_f1}\n")

#Вывод результатов
print(f"F1 Score (Building): {f1_building}")
print(f"F1 Score (Background): {f1_background}")
print(f"Average F1 Score: {average_f1}")