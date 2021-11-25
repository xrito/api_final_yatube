## Описание API проекта Yatube

API позволяет предоставлять данные в платформонезависимом виде.
Проект дает возможность:
Подписываться на пользователя.
Просматривать, создавать новые, удалять и изменять посты.
Просматривать группы.
Комментировать, смотреть, удалять и обновлять комментарии.

## Установка 
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

## Примеры
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
