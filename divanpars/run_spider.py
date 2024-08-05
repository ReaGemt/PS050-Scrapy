import os
import datetime
import csv
from openpyxl import Workbook

# Имя паука
spider_name = "svetnewpars"

# Генерация уникального имени файла на основе текущей даты и времени
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"output_{current_time}.csv"
xlsx_filename = f"output_{current_time}.xlsx"

# Формирование команды для запуска Scrapy
command = f"scrapy crawl {spider_name} -o {csv_filename}:csv -s FEED_EXPORT_ENCODING=utf-8"

# Выполнение команды
os.system(command)

print(f"Data has been saved to {csv_filename}")

# Чтение данных из CSV и запись в XLSX
workbook = Workbook()
sheet = workbook.active

with open(csv_filename, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        sheet.append(row)

workbook.save(xlsx_filename)
print(f"Data has also been saved to {xlsx_filename}")
