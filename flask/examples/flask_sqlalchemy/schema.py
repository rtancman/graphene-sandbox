import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel
from database import db_session


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel


class Query(graphene.ObjectType):
    employee = graphene.Field(Employee, id=graphene.ID(required=True))
    department = graphene.Field(Department, id=graphene.ID(required=True))
    role = graphene.Field(Role, id=graphene.ID(required=True))
    employees = graphene.List(Employee)
    departments = graphene.List(Department)
    roles = graphene.List(Role)

    def resolve_employee(self, info, **kwargs):
        query = Employee.get_query(info)
        return query.get(kwargs.get('id'))

    def resolve_department(self, info, **kwargs):
        query = Department.get_query(info)
        return query.get(kwargs.get('id'))

    def resolve_role(self, info, **kwargs):
        query = Role.get_query(info)
        return query.get(kwargs.get('id'))

    def resolve_employees(self, info):
        query = Employee.get_query(info)
        return query.all()

    def resolve_departments(self, info):
        query = Department.get_query(info)
        return query.all()

    def resolve_roles(self, info):
        query = Role.get_query(info)
        return query.all()


class CreateEmployee(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    employee = graphene.Field(lambda: Employee)

    def mutate(root, info, **kwargs):
        employee = EmployeeModel(**kwargs)
        db_session.add(employee)
        db_session.commit()
        return CreateEmployee(employee=employee)


class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()


schema = graphene.Schema(query=Query, mutation=Mutation,
                         types=[Department, Employee, Role])
