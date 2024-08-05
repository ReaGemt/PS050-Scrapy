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
Запуск паука

Вы можете запустить паука svetnewpars следующей командой:

```
scrapy crawl svetnewpars
```
Для экспорта данных в CSV-файл с уникальным именем:

```
python run_spider.py
```
Это создаст файл с именем output_<дата_время>.csv, содержащий собранные данные.
Содержание паука

Файл svetnewpars_spider.py содержит паука, который:

    Собирает информацию о светильниках, включая название, цену и URL.

Основные селекторы

Убедитесь, что селекторы в svetnewpars_spider.py соответствуют структуре страницы:

```
svets = response.css('div._Ud0k')

for svet in svets:
    yield {
        'name': svet.css('div.lsooF span::text').get(),
        'price': svet.css('div.pY3d2 span::text').get(),
        'url': response.urljoin(svet.css('a::attr(href)').get())
    }
```
