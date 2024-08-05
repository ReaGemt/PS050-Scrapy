import os
import datetime

# Имя паука
spider_name = "svetnewpars"

# Генерация уникального имени файла на основе текущей даты и времени
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"output_{current_time}.csv"

# Формирование команды для запуска Scrapy
command = f"scrapy crawl {spider_name} -o {output_filename}:csv -s FEED_EXPORT_ENCODING=utf-8"

# Выполнение команды
os.system(command)

# Проверка и пере-энкодирование если необходимо
with open(output_filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Пере-энкодирование в utf-8 (если это необходимо, обычно уже utf-8)
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Data has been saved to {output_filename}")
