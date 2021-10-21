<h2 align="center">Тестовое задание от @ya_godless</h2>

Запуск:
	python3 -m venv env
	sourse env/bin/activate
	pip install djangorestframework
	git pull https://github.com/yaroslavgodless/fr_test.git
	cd fr_test
	python3 manage.py runserver
enjoy =3

<p>Небольшая документация:</p>
<li>http://127.0.0.1:8000/api/v1/questionnaire/ - список доступных опросников</li>
<lш>http://127.0.0.1:8000/api/v1/questionnaire/*циферка - подробности самого опросника</li>
<li>http://127.0.0.1:8000/api/v1/answer/*циферка - Post/Get запрос определенного вопроса</li>

<p>Доступ к бд:</p>
user:fr_test

password:12345
