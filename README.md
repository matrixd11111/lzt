# LZT with Docker: Django, Postgres, Gunicorn,  Nginx

###Как установить Docker на Linux :
```
Сначала обновляем существующий перечень пакетов:
	sudo apt update

Затем устанавливаем необходимые пакеты, которые позволяют apt использовать пакеты по HTTPS:
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	
Затем добавляем в свою систему ключ GPG официального репозитория Docker:
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Добавляем репозиторий Docker в список источников пакетов APT:
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

Затем обновим базу данных пакетов информацией о пакетах Docker из вновь добавленного репозитория:
	sudo apt update
	
Далее устанавливаем Docker:	
	sudo apt install docker-ce -y
	
Чтобы не вводить sudo каждый раз при запуске команды docker, добавьте имя своего пользователя в группу docker:
	sudo usermod -aG docker ${USER}

Проверим что служба успешно запустилась:
	sudo service docker status
	
```


### How to install Docker on Linux:
First, update the existing list of packages:
apt update

Then install the necessary packages that allow apt to use packages over HTTPS:
apt install apt-transport-https ca-certificates curl software-properties-common

Then we add the GPG key of the official Docker repository to our system:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Add the Docker repository to the list of APT package sources:
sudo add-apt-repository "deb [arch = amd64] https://download.docker.com/linux/ubuntu bionic stable"

Next, update the package database with Docker package information from the newly added repository:
apt update

Next, install Docker:
sudo apt install docker-ce -y

To avoid typing sudo every time you run the docker command, add your username to the docker group:
sudo usermod -aG docker $ {USER}

Check that the service started successfully:
sudo service docker status


### Run docker-compose
```
version: '3.7'

services:
  web:
    build:
      context: ./app
    command: gunicorn hello_django.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - static_volume:/home/app/web/staticfiles
      - media_volume:/home/app/web/mediafiles
    expose:
      - 8000
    env_file:
      - ./.env
    depends_on:
      - db
  db:
    image: postgres:12.0-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    env_file:
      - ./.env.db
  nginx:
    build: ./nginx
    volumes:
      - static_volume:/home/app/web/staticfiles
      - media_volume:/home/app/web/mediafiles
    ports:
      - 8181:80
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```
Запуск докер-образа:
	docker-compose -f docker-compose.yml up -d --build

    Test it out at [http://127.0.0.1:8181/](http://127.0.0.1:8181/). 

### Run docker swarm

    ```
    $ docker build -t web_django -f app/Dockerfile app/
    $ docker build -t nginx_django nginx/
    $ docker stack deploy --compose-file docker-swarm-compose.yml django_test
    ```

    Test it out at [http://127.0.0.1:8181/](http://127.0.0.1:8181/). 


# для тех у кого линукс и кто хочет локально запустить без докера
# !!требуется проверка со стороны спецов по развертыванию!!
# пройдёт ли на такой конфигурации

# чтобы не портить свой комп, ставим виртуальное окружение
python3 -m venv env
# активируем виртуальное окружение
source env/bin/activate
# находясь в корне проекта, в BASH экспортируем все переменные окружения
eval export `cat .env`
# устанавливаем все зависимости, которые требуются для проекта
pip install -r ./app/requirements.txt 
# создаём миграции
python ./app/manage.py makemigrations
# проводим миграции
python ./app/manage.py migrate
# запускаем локальный сервер
python ./app/manage.py runserver

#### 
Дополнил (Linar)
1) sudo pip3 install -r requirements.txt
2) python3 manage.py makemigrations
3) python3 manage.py migrate
4) python3 manage.py createsuperuser
5) python3 manage.py runserver
