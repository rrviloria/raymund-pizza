# pizza-api

This is the main repository for Raymund's Pizzas

## Development environment


This was initially created using:

* Docker version 18.09.2
* docker-compose version 1.23.2


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

## Additional information

Package versions are specified in Dockerfile / Pipfile and this is just for refference, but containerised application is using:

| Name                   | Version   |
| ---                    | ---       |
| Python                 | 3.7.7     |
| PostgreSQL             | 11.3      |
| Django                 | 2.2.2     |
