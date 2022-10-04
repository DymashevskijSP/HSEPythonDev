# Проект для курса по веб-разработке
## Сервис для планирования
Можем создавать встречи, добавлять людей, смотреть свои и чужие встречи и так далее(более подробный функционал появится в процессе разработки)
## текущие entry point 
 1. GET test/hello/hello_world -- возвращает {"message": "hello, world!"}
 2. POST test/hello/hello_world (Content-type: application/json, нужен параметр 'text': string) -- возвращает {"message": text}

необходимые зависимости в файлах Pipfile и Pipfile.lock
позже появится docker образ
для запуска сервера достаточно написать python manage.py runserver

В текущей конфигурации сложной бизнес-логики нет,для нее нужна база данных, поэтому ручки моковые, однако тесты на них есть уже сейчас, для их запуска надо выполнить

python -m unittest HSEPythonDev/tests/functional/<test_name> (<test_name> соответствует файлу с тестами, например test_meetings.py)
