import graphene
from graphene_django.types import DjangoObjectType
from services.pizza.models import Pizza, Transactions
from services.pizza.model_types import PizzaType


class PizzaQuery(graphene.ObjectType):
    all_pizzas = graphene.List(PizzaType)

    def resolve_all_pizzas(self, info, **kwargs):
        return Pizza.objects.all().order_by('-transactions')
