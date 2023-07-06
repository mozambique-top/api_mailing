REST API для системы сервиса рассылок уведомлений
<<<<<<< HEAD
=====

Функциональные требования
----------
[Ссылка на техническое задание](https://www.craft.do/s/n6OVYFVUpq0o6L)

Описание проекта
----------
=======
Функциональные требования
https://www.craft.do/s/n6OVYFVUpq0o6L

Описание проекта
>>>>>>> 2ec733be5053c0351f3bc03a568f82c89ecb0762
Проект состоит из проектируемого API сервиса для работы с данными клиентов и управления рассылками сообщений.

API сервис реализуется на базе фреймворка DRF.

Системные требования
<<<<<<< HEAD
----------

* Python 3.6+
* Docker
* Works on Linux, Windows, macOS, BS

Стек технологий
----------

* Python 3.8
* Django 3.1
* Django Rest Framework
* PostreSQL
* Nginx
* gunicorn
* Docker
* Сelery
* Redis

Установка проекта из репозитория (Linux и macOS)
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash 
git clone git@github.com:mozambique-top/api_mailing.git

cd api_mailing
```
Токен для сервиса отправки сообщений согласно ТЗ
```bash 
echo SENDING_API_TOKEN=****************** >> .env
```

3.Установка и запуск приложения в контейнерах:
```bash 
docker-compose up -d
```

4.Запуск миграций и сбор статики:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input 
```
Документация к проекту
----------
Документация для API после установки доступна по адресу: 

```http://127.0.0.1/redoc/```
=======
Python 3.6+
Docker
Works on Linux, Windows, macOS, BS
Стек технологий
Python 3.8
Django 3.1
Django Rest Framework
PostreSQL
Nginx
gunicorn
Docker
Сelery
Redis
Установка проекта из репозитория (Linux и macOS)
Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/mozambique-top/api_mailing.git

cd API_Mailings_TW
cd infra

Токен для сервиса отправки сообщений согласно ТЗ

echo SENDING_API_TOKEN=****************** >> 
Установка и запуск приложения в контейнерах:
docker-compose up -d
Запуск миграций и сбор статики:
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input 
Документация к проекту
Документация для API после установки доступна по адресу:

http://127.0.0.1/redoc/
>>>>>>> 2ec733be5053c0351f3bc03a568f82c89ecb0762
