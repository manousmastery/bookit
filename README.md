# bookit

## Setup + Installation
- if you are on MAC Intel, make sure you have brew install, follow instructions on this [link](https://brew.sh/)
- In a terminal run the following:
```angular2html
brew install pyenv mongodb-community mongodb-database-tools mongosh pdm openssl
```

- Install python version with:
```angular2html
pyenv install 3.10.0
```
- Set it as a default version
```angular2html
pyenv global 3.10.0
```


## Development
**Install dependencies**
```
pdm install
```

**Generate migration file if changes on model**
```
python manage.py makemigrations
```


**Run migration**
```
python manage.py migrate
```


**Run server**
```
python manage.py runserver
```


**Linting + import optimizer**
```
ruff check 
```
