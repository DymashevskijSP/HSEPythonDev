# Проект для курса по веб-разработке
## текущие entry point 
 1. GET test/hello/hello_world -- возвращает {"message": "hello, world!"}
 2. POST test/hello/hello_world (Content-type: application/json, нужен параметр 'text': string) -- возвращает {"message": text}

необходимые зависимости в файлах Pipfile и Pipfile.lock
позже появится docker образ
для запуска сервера достаточно написать python manage.py runserver