import graphene
from flask import Flask
from flask_graphql import GraphQLView


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()

    person = graphene.Field(lambda: Person)

    def mutate(root, info, **kwargs):
        person = Person(**kwargs)
        return CreatePerson(person=person)


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

    def resolve_person(parent, info, **kwargs):
        return Person(name='Tancman', age=21)


schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.debug = True


app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


if __name__ == "__main__":
    app.run()
