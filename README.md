# python3_pipenv_flask_appfactory_celery_boilerplate

## Prerequisites
* [Python 3.7.*](https://www.python.org/downloads/)
* [pipenv](https://docs.pipenv.org/)
* [Celery](http://www.celeryproject.org/)


**Quickstart (using MacOS and `brew`)**

`brew install python3 pipenv rabbitmq`

## Installation
From the root of the project execute:

**Python dependencies**

`pipenv install`


**RabbitMQ (using MacOS and `brew`)**
```
brew services start rabbitmq
```

## Run application

`make run`: Runs the Flask web application, 10 Celery workers and 1 Celery Scheduler on port `5000`