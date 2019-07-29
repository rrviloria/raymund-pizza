#!/bin/sh
# run-seed.sh

echo "Eating all pizzas, yummy"
docker exec -it raymundpizza_web_1 pipenv run python manage.py flush --no-input


echo "Creating pizzas. please wait"
docker exec -it raymundpizza_web_1 pipenv run python seed.py