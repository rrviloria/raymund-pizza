from django_seed import Seed

import django
import os
import random
import decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza_api.settings")
django.setup()

seeder = Seed.seeder()

from services.pizza.models import Pizza, PizzaType

types = ('CALIFORNIA', 'CHICAGO', 'NEW YORK',)

seeder.add_entity(PizzaType, 5, {
    'name': lambda x: types[random.randint(0, 2)],
})

inserted_pks = seeder.execute()
pizza_type_ids = inserted_pks[PizzaType]

seeder.add_entity(Pizza, 5, {
    'name': lambda x: 'pizza-%s' % random.randint(1, 50),
    'price': lambda x: decimal.Decimal(random.randrange(155, 389)) / 100,
    'pizza_type_id': lambda x: pizza_type_ids[random.randint(0, len(pizza_type_ids) - 1)],
})

seeder.execute()
