import os
import datetime

# Имя паука
spider_name = "svetnewpars"

# Генерация уникального имени файла на основе текущей даты и времени
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"output_{current_time}.csv"

# Формирование команды для запуска Scrapy
command = f"scrapy crawl {spider_name} -o {output_filename}:csv"

# Выполнение команды
os.system(command)

print(f"Data has been saved to {output_filename}")
