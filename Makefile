BASEDIR=$(CURDIR)
DOCDIR=$(BASEDIR)/docs
DISTDIR=$(BASEDIR)/dist


check:
	pre-commit run --show-diff-on-failure --color=always --all-files

update:
	poetry up
	pre-commit autoupdate

create:
	docker-compose -f docker-compose.yml up -d --build

start:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down -v

superuser:
	docker exec -it app poetry run python backend/manage.py createsuperuser

generate-fake-data:
	docker exec -it app poetry run python backend/manage.py generate_fake_data
