# Тестовое задание для Bewise

Сервис запускается командой `docker-compose up`
***

## Postgres
PostgreSQL хостится на порту
* Адрес: http://0.0.0.0:5432
* База данных: `bewisedb`
* Пользователь: `bewise`
* Пароль: `bewise`

Для доступа к базе данных можно использовать pgadmin:
* Адрес: http://0.0.0.0:5050
* Email: `user@test.com`
* Пароль: `bewise`
***

## API
* Интерактивный режим работы с API:
http://0.0.0.0:5000/docs

POST-запрос для добавления вопросов в бд:  

    curl --location --request POST '0.0.0.0:5000/questions' \
    --header 'Content-Type: text/plain' \
    --data-raw '{
      "questions_num": 1
    }'

Примет ответа:  

    {
        "id": 3,
        "created_at": "2022-05-08T15:55:27.977510",
        "question": "He's Augie Doggie's father",
        "answer": "Doggie Daddy"
    }
    
