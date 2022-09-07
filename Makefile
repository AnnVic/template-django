help:
	@echo "Chat service"
	@echo "usage: make COMMAND"
	@echo ""
	@echo "Commands:"
	@echo "  db.migrate         Migrate db"
	@echo "  db.make_migrations Make migrations"
	@echo "  app.start          Create new module"
	@echo "  pip.freeze         Freeze dependencies"
	@echo "  pip.install        Install dependencies"
	@echo "  mypy.run           Run mypy analyzer"

db.make_migrations:
	@docker-compose exec app python3 manage.py makemigrations
db.migrate:
	@docker-compose exec app python3 manage.py migrate

app.start:
	@docker-compose exec app mkdir src/$(name)
	@docker-compose exec app django-admin startapp $(name) src/$(name)

pip.freeze:
	@docker-compose exec app pip3 freeze > requirements.txt

pip.install:
	@docker-compose exec app pip3 install -r requirements.txt

mypy.run:
	@docker-compose exec app mypy

pylint.run:
	@docker-compose exec app pylint src

black.run:
	@docker-compose exec app black src

code.analyse:
	@make black.run
	@make mypy.run
	@make pylint.run

up:
	@docker-compose up -d --build --force-recreate
