

# **Проект парсинга на Scrapy** 

## Описание
___
Парсинг может получать информацию об PEP, номер, название, статус, так же подсчитывает столько статусов на данный момент и их общее количество.
___
## Технологии
___
-  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
- Scrapy



___
## Установка и запуск
___
1. Склонируйте репозиторий на свой компьютер:
```bash 
git clone git@github.com:ShlykovDmitriy/scrapy_parser_pep.git
```

2. Создайте виртуальное окружение в корне проекта и активируйте его :

```bash 
python -m venv venv
source venv/bin/activate
```

3. Установите зависимости :


```bash
pip install -r requirements.txt
``` 


4. Запуск программы:


```bash
scrapy crawl pep
```
С результатами можно ознакомиться в папке results



___
### Автор
___
[Шлыков Дмитрий](https://github.com/ShlykovDmitriy)