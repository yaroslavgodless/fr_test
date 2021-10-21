# fr_test
Тестовое задание от @ya_godless
Запуск:
	python3 -m venv env
	sourse env/bin/activate
	pip install djangorestframework
	git pull https://github.com/yaroslavgodless/fr_test.git
	cd fr_test
	python3 manage.py runserver
enjoy =3

Небольшая документация:
http://127.0.0.1:8000/api/v1/questionnaire/ - список доступных опросников
http://127.0.0.1:8000/api/v1/questionnaire/*циферка - подробности самого опросника
http://127.0.0.1:8000/api/v1/answer/*циферка - Post/Get запрос определенного вопроса

Доступ к бд:
user:fr_test
password:12345
