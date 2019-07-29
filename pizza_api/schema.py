import graphene
import graphql_jwt
import services.pizza.queries
import services.pizza.mutations


class Query(services.pizza.queries.PizzaQuery, graphene.ObjectType):
    pass


class Mutation(services.pizza.mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
