#!/bin/sh
# seed.sh

echo "Eating all pizzas, yummy"
docker exec -it pizza_web_1 pipenv run python manage.py flush --no-input


echo "Creating pizzas. please wait"
docker exec -it pizza_web_1 pipenv run python seed.py