## API для проекта социальной сети YaTube, основанный на Django-Rest-Framework

API позволяет предоставлять данные в платформонезависимом виде.
Польза проекта в том, что он дает пользоваться функционалом приложения не посещая сайт.
Реализован функционал дающий возможность:
* Подписываться на пользователя.
* Просматривать, создавать новые, удалять и изменять посты.
* Просматривать и создавать группы.
* Комментировать, смотреть, удалять и обновлять комментарии.
* Фильтровать по полям.
#### К API есть документация по адресу http://localhost:8000/redoc/

Функционал включает в себя:
Авторизацию по JWT (JSON Web Token) токену
Сериализацию данных для всех моделей проекта (Post, Comment, Group, Follow)
Обработку GET, POST, PATCH, PUT и DELETE запросов к базе данных YaTube


### Стек технологий

* Python +Django REST Framework
* библиотека Simple JWT - работа с JWT-токеном
* система управления версиями - git

### Установка 
Клонировать репозиторий и перейти в него в командной строке:

```$ git clone https://github.com/xrito/api_final_yatube.git```

```$ cd yatube_api```

 Cоздать и активировать виртуальное окружение:
 
 ```$ python -m venv venv```
  ```$source venv/Script/activate```
  
 Установить зависимости из файла requirements.txt:

```$ pip install -r requirements.txt```

Выполнить миграции:

```$ python manage.py migrate```

Запустить проект:

```$ python manage.py runserver```

### Примеры
Для создания примеров использована программа Postman (https://web.postman.co/)
#### Получаем токен

Отправляем POST-запрос на адрес ```/api/v1/jwt/create/``` и передаем 2 поля в `Body`. 

`username - имя пользователя.`
`password - пароль пользователя.`

![This is an image](https://i.ibb.co/JQS4pSJ/2021-11-25-14-21-23.png)

Во вкладке Authorization добавляем полученные токен: `Bearer <токен>`

#### Создание поста

Передаем POST-запрос:

* __"text": "string",__
* __"group": 1__

![This is an image](https://i.ibb.co/dM3YX3M/2021-11-25-14-34-52.png)

#### К API есть документация по адресу http://localhost:8000/redoc/

### Автор

[![Telegram](https://img.shields.io/badge/-Telegram-464646?style=flat-square&logo=Telegram)](https://t.me/harkort)
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/xrito)  


[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![pytest](https://img.shields.io/badge/-pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?style=flat-square&logo=SQLite)](https://www.sqlite.org/)
