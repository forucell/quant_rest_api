# Quant Service


## Features

- [Flask](http://flask.pocoo.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [postegresql](https://www.postgresql.org)
- [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

## Installation

### Requirements

- Python^=3.7
- Postegresql^=10.5

### Commands

- Download source code from github account.

    ```bash
    $ git clone https://github.com/forucell/quant-rest-api.git
    ```

- Go to project folder and set python environment

    ```bash
    $ cd quant-rest-api
    $ python3 -m venv venv
    ```

- Create .env file and fill out with necessary information

    ```bash
    $ touch .env
    ```
    

    ```.env

    USERNAME=postgres
    PASSWORD=****
    HOST=localhost
    PORT=5432
    DBNAME=test

    ```

## Running

Runt with gunicorn

    ```bash
    # Debugging mode
    (venv) $  gunicorn --log-level debug --reload --bind 0.0.0.0:5000 quant.wsgi:app
    # Production mode
    (venv) $  gunicorn --bind 0.0.0.0:5000 quant.wsgi:app &
    ```



### Docker

#### Requirement

- Docker

#### Docker Build

```.bash
docker build -t quant/app:{VERSION} .
```

#### Docker run

```.bash
docker run -d -p {PORT}:80 --name quant_app quant/app:{VERSION} 
```