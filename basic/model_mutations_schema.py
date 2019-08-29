import graphene


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


if __name__ == '__main__':
    result = schema.execute('''
    mutation myFirstMutation {
        createPerson(name:"Peter", age: 18) {
            person {
                name
                age
            }
        }
    }
    ''')
    print(result.data)
