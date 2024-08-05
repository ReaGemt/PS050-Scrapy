# Scrapy Project: divanpars

Этот проект Scrapy предназначен для сбора данных о светильниках с сайта [divan.ru](https://www.divan.ru/category/svet).

## Структура проекта

- divanpars/                # Корневая папка проекта
    - scrapy.cfg            # Конфигурационный файл
    - divanpars/            # Пакет проекта Scrapy
        - __init__.py
        - items.py
        - middlewares.py
        - pipelines.py
        - settings.py
        - spiders/          # Папка с пауками
            - __init__.py
            - svetnewpars_spider.py



- `scrapy.cfg`: Конфигурационный файл Scrapy.
- `README.md`: Этот файл, содержащий описание проекта и инструкции.
- `run_spider.py`: Скрипт для запуска паука с автоматической генерацией уникального имени файла CSV.
- `divanpars/`: Основная директория проекта Scrapy.
- `spiders/`: Папка, содержащая паука `svetnewpars`.

## Установка и настройка

### 1. Клонирование репозитория

Сначала клонируйте репозиторий на ваш локальный компьютер:

```
git clone <URL репозитория>
cd divanpars
```
2. Создание виртуальной среды

Рекомендуется использовать виртуальную среду для управления зависимостями:

```
python -m venv .venv
```
3. Активация виртуальной среды

    Windows:

```
.venv\Scripts\activate
```
Unix/MacOS:

```
source .venv/bin/activate
```
4. Установка зависимостей

Установите необходимые пакеты из requirements.txt:

```
pip install -r requirements.txt
```
5. Настройка Scrapy

Убедитесь, что файл scrapy.cfg корректно настроен:

```
[settings]
default = divanpars.settings
```
### Запуск паука
Запуск Scrapy через командную строку

Вы можете запустить паука svetnewpars следующей командой:
```
scrapy crawl svetnewpars -o output.csv -s FEED_EXPORT_ENCODING=utf-8
```

### Запуск Scrapy через run_spider.py

Запустите скрипт run_spider.py, чтобы автоматически собрать данные и сохранить их в файлы CSV и XLSX:

```
python run_spider.py
```
Этот скрипт создаст файлы с именами `output_<дата_время>.csv` и `output_<дата_время>.xlsx`, содержащие собранные данные.


### Описание паука

Файл svetnewpars_spider.py содержит паука, который:

    Собирает информацию о светильниках, включая название, цену и URL.
    Переходит на следующую страницу, если она существует, используя пагинацию.