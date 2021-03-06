# Practica final
Verificación y desarrollo de programas

## Setup

1. Clone the repo
2. Be sure you have installed [virtualenv](https://virtualenv.pypa.io/en/latest/) in your machine:
```
pip install virtualenv
```
3. Install and active the virtualenv for your project 
```
rm -rf venv
virtualenv venv
source venv/bin/activate
```
4. Install the requirements into your project
```
pip install -r requirements.txt
```

5. Run Redis service & client
```
redis-server
redis-cli
```

## Run Tests
Unit Tests
```
venv/bin/py.test tests/game_tests.py
or
venv/bin/nosetests tests/game_tests.py

```
BDD Tests
```
lettuce tests
```

## Pylint
```
venv/bin/pylint juego/game.py
```

# Coverage
```
cd juego
venv/bin/coverage run game.py
venv/bin/coverage report game.py
```
