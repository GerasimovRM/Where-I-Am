# Where-I-Am

Пока приложение умееть лишь регистрировать пользователей, авторизовать (через JWT токен, см. далее), получить данные других пользователей, добавлять их в друзья, смотреть заявки в друзья. Дружественность в приложении в одну сторону!

## JWT-токен

Для авторизации пользователя необходимо сохранить jwt access token в хедеры запроса:
'Authorization': 'Bearer <jwt_access_token>' 

## Развертка приложения

Приложение развернуто в heroku. Работа с ним доступна по по URL: https://wia-perm.herokuapp.com/api/v1

## Основные запросы

get: /user/<int:user_id> - показать информацию о пользователе
delete: /user/<int:user_id> - удалить пользователя (только для администрации)

get: /user - получить информацию о себе

get: /users - получить всех пользователей
post: /users - добавить пользователя (только для администрации)

post: /signup - регистрация пользователя

get: /signin - аворизация пользователя

get: /admins - показать администраторов (только для администрации)

get: /friends - отразить список друзей

post: /friend_add/<int:friend_id> - добавить в друзья пользователя

get: /friends_check - список пользователей, которые добавили текущего в друзья, но текущий не добавил их
