# pizza-api

This is the main repository for Raymund's Pizzas

## Development environment


This was initially created using:

* MacOs version 10.12.6
* Docker version 17.12.0
* docker-compose version 1.18.0


1) Clone this repo
2) In the main directory (near `manage.py`) create a `.env` file with the following contents:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_HOST=db
DB_PORT=5432

```

3) run `docker-compose up`
4) visit `http://localhost:8000`

## Running seed
Instructions on how to seed data can be seen here https://github.com/rrviloria/raymund-pizza/wiki/Running-seed


## Running tests
Instructions on how to seed data can be seen here https://github.com/rrviloria/raymund-pizza/wiki/Running-tests


## GrahpQL APIs
Instructions on how to query GraphQL Pizza APIs can be seen here https://github.com/rrviloria/raymund-pizza/wiki/Query-GraphQL-APIs


## Additional information

Package versions are specified in Dockerfile / Pipfile and this is just for refference, but containerised application is using:

| Name                   | Version   |
| ---                    | ---       |
| Python                 | 3.7.7     |
| PostgreSQL             | 11.3      |
| Django                 | 2.2.2     |
