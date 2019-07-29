import graphene
from services.pizza.models import PizzaType, Pizza
from services.pizza.model_types import PizzaType as PizzaT, PizzaTypeType


class CreatePizzaTypesMutation(graphene.relay.ClientIDMutation):
    pizza_type = graphene.Field(PizzaTypeType)

    class Input:
        name = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        pizza_type = PizzaType.objects.create(**input)
        return cls(pizza_type=pizza_type)


class CreatePizzaMutation(graphene.relay.ClientIDMutation):
    pizza = graphene.Field(PizzaT)

    class Input:
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        pizza_type_id = graphene.Int(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        pizza = Pizza.objects.create(**input)
        return cls(pizza=pizza)


class Mutation(graphene.ObjectType):
    create_pizza_type = CreatePizzaTypesMutation.Field()
    create_pizza = CreatePizzaMutation.Field()
