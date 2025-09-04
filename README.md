# DjangoVueRestAPI
Treinando Django e Vue como backend e frontend respectivamente

# Com base no tutorial de Django(REST API) + Vue.js do Leonardo Lourenco + https://tutorial.djangogirls.org/en/deploy/
# https://github.com/Leonardo-Lourenco/rest-api-django-vueJS

# Documentações:

https://axios-http.com/ptbr/docs/intro - Axios<br>
https://vuejs.org/guide/quick-start - Vue.js<br>
https://nodejs.org/docs/latest/api/- Node<br>
https://tailwindcss.com/showcase - Tailwind<br>
https://docs.djangoproject.com/en/5.2/ - Django<br>
https://tutorial.djangogirls.org/en/deploy/ - Tutorial DjangoGirls para subir um blog<br>
https://help.pythonanywhere.com/pages/ - PythonAnywhere<br>
https://docs.docker.com/ - Docker<br>
Fiz um arquivo relatando o que fiz em backend seguindo o tutorial djangogirls + tutorial do leo
E um tambem para o frontend, os dois em txt

# TUTORIAL DOCKER
git clone https://github.com//FeLiXp90/DjangoVueRestAPI.git<br>
cd ../backend<br>
mv .env.example .env<br>
cd .. (Volte para a pasta raiz 'DjangoVueRestAPI'<br>
docker-compose up --build

# TUTORIAL LOCAL

python3 -m venv venv<br>
venv\Scripts\Activate.ps1<br>
cd ../backend<br>
mv .env.example .env<br>
pip install -r requirements.txt

# Criar o banco/executar backend localmente: 
python3 manage.py migrate<br>
python3 manage.py makemagrations<br>
Criar Admin:<br>
python3 manage.py createsuperuser<br>
python3 manage.py runserver

# Executar frontend localmente:
cd ..<br>
cd frontend<br>
npm install<br>
npm run serve
