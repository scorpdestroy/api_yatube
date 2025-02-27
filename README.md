REST API YaTube 
=====

Системные требования
----------
* Python 3.11

Стек технологий
----------
* Python 3.11
* Django 2.2 
* Django Rest Framework
* Pytest
* Simple-JWT
* SQLite3

Установка проекта (Linux)
----------

1. Клонировать репозиторий:
```bash
git clone git@github.com:NikitaChalykh/API_YaTube.git
cd API_YaTube
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env

source env/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd yatube_api

python3 manage.py migrate
```
5. Запустить проект (в режиме сервера Django):
```bash
python3 manage.py runserver
```

