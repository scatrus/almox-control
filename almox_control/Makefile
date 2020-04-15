
.PHONY: clean install sandbox test coverage docs build_release, publish_release_testpypi publish_release

clean:
	find . -name '*.pyc' -delete
	find ~ -path './__pycache__/*' -not -path "*/venv/*" -delete
	find ~ -type d -name '__pycache__' -delete
	rm -Rf *.egg-info
	rm -Rf dist/
	rm -Rf build/

cache:
	git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch <file/dir>' HEAD

reset:
	find . -name '*.sqlite3' -delete
	find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*/venv/*" -delete

run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate --run-syncdb
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'email@email.com', 'admin')" | python manage.py shell
