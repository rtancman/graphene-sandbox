from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(name=String())

    def resolve_hello(root, info, name):
        return f'Hello {name}!'


schema = Schema(query=Query)


if __name__ == '__main__':
    query = '''
        {
            hello(name: "GraphQL")
        }
    '''
    result = schema.execute(query)
    print(result.data)
