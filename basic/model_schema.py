from graphene import ObjectType, String, Field, Schema, Int


class Person(ObjectType):
    first_name = String()
    last_name = String()


class Query(ObjectType):
    my_best_friend = Field(Person, id=Int(required=True))

    def resolve_my_best_friend(parent, info, **kwargs):
        return {"first_name": "Lala", "last_name": "Lele"}


schema = Schema(query=Query)


if __name__ == '__main__':
    result = schema.execute('''
        {
            myBestFriend(id: 1) {
                firstName
                lastName
            }
        }
    ''')
    print(result.data)
