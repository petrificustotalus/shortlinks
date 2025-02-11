# SHORTLINKS
###### This repository contains API code for creating short urls.
----

## How to run
### Create a .env file with the following variables:
```
POSTGRES_DB={POSTGRES_DB}
POSTGRES_USER={POSTGRES_USER}
POSTGRES_PASSWORD={POSTGRES_PASSWORD}
POSTGRES_HOST={POSTGRES_HOST}
PORT={PORT}
```

### Requirements
- Pyenv
- Python 3.12
- Poetry 1.8.3
- Docker

## Local environement setup:
- navigate to the project repository
- `pyenv install 3.12` if not already installed
- `pyenv local 3.12`
- `poetry shell`
- `poetry install`

## Run using Docker
- navigate to the project repository
- `docker-compose build`
- `docker-compose up -d`

## Run pytest localy:
- setup local environement
- export ENV=testing
- make sure `postgres-test` is up
- run `pytest`
