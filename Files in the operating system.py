import os
import time

directory = '.'  # Переменная с путем к директории

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # Формируем полный путь к файлу
        filetime = os.path.getmtime(filepath)  # Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Преобразуем время в нужный формат
        filesize = os.path.getsize(filepath)  # Получаем размер файла
        parent_dir = os.path.dirname(filepath)  # Получаем родительскую директорию файла
        print(f'Обнаружен файл: {file}, '
              f'Путь: {filepath}, '
              f'Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
