import graphene
from services.pizza.models import PizzaType as PizzaTypeModel, Pizza, Transactions
from graphene_django import DjangoObjectType
from django.db.models import Sum
from pizza_api.settings import *


class PizzaType(DjangoObjectType):
    pizza_type = graphene.String()
    total_sold = graphene.Int()
    total_amount = graphene.Decimal()
    time_zone = graphene.String()  # unrelated attribute :)

    class Meta:
        model = Pizza

    def resolve_pizza_type(root, info, **input):
        return root.pizza_type.name

    def resolve_total_sold(root, info, **input):
        return root.transactions_set.count()

    def resolve_total_amount(root, info, **input):
        return root.transactions_set.aggregate(Sum('price'))['price__sum']

    def resolve_time_zone(root, info, **input):
        return TIME_ZONE


class PizzaTypeType(DjangoObjectType):
    class Meta:
        model = PizzaTypeModel
