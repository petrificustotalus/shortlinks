# SHORTLINKS
###### This repository contains API code for creating short urls.
----

## How to run

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
- make sure `postgres-test` is up
- run `pytest`
