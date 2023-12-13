# scrapy_parser_pep

Это Scrapy парсер, собирающий данные о статусах PEP с официального сайта.
Данные собираются в два csv-файла:
 - в первом в формате Номер, Имя, Статус
 - во втором подсчитывается количество PEP в каждом статусе, формат в файле - Статус, Количество. Также подсчитано общее количество PEP.

## Технологии
- Python
- Scrapy

### Установка
Склонировать репозиторий
```
https://github.com/smirnovds1990/scrapy_parser_pep
```

Установка виртуального окружения и зависимостей:
```
python -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

Запуск парсера:
перейти в папку `scrapy_parser_pep`, запустить парсер:
```
scrapy crawl pep
```


###### Автор проекта
[smirnovds](https://github.com/smirnovds1990)