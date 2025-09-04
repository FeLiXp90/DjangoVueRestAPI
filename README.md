# DjangoVueRestAPI
Treinando Django e Vue como backend e frontend respectivamente

# Com base no tutorial de Django(REST API) + Vue.js do Leonardo Lourenco
# https://github.com/Leonardo-Lourenco/rest-api-django-vueJS

# Documentações:

https://axios-http.com/ptbr/docs/intro - Axios

https://vuejs.org/guide/quick-start - Vue.js

https://nodejs.org/docs/latest/api/- Node

https://tailwindcss.com/showcase - Tailwind

https://docs.djangoproject.com/en/5.2/ - Django

https://tutorial.djangogirls.org/en/deploy/ - Tutorial DjangoGirls para subir um blog

https://help.pythonanywhere.com/pages/ - PythonAnywhere

https://docs.docker.com/ - Docker

Fiz um arquivo relatando o que fiz em backend seguindo o tutorial djangogirls + tutorial do leo
E um tambem para o frontend, os dois em txt

# Criar o banco para funcionar localmente: 
python3 manage.py migrate
python3 manage.py makemagrations
Criar Admin:
python3 manage.py createsuperuser
python3 manage.py runserver

# Para criar um containers para o projeto com DOCKER:
cd path...\DjagoVueRestAPI\Django_Vue
docker-compose up --build

