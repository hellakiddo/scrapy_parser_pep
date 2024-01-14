![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scrapy](https://img.shields.io/badge/Scrapy-3670A0?style=for-the-badge&logo=scrapy&logoColor=white)

# Асинхронный парсинг документации Python

### Парсер выполняет сбор данных со страницы о PEP https://peps.python.org/ и сохраняет ее в формате CSV.

### Как запустить проект:
Клонируем репозиторий:
```python
git@github.com:Amir800S/scrapy_parser_pep.git
```
Создать, активировать виртуальное окружение и установить зависимости:
```python
python -m venv venv
```
```python
venv/Scripts/activate
```
```python
pip install -r requirements.txt 
```
### Запускаем парсер
```python
scrapy crawl pep
```

### Автор: [Сосламбеков Амир](https://github.com/Amir800S)