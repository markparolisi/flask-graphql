import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Department as DepartmentModel, Employee as EmployeeModel

class Department(SQLAlchemyObjectType):
    class Meta(object):
        model = DepartmentModel
        interfaces = (relay.Node,)

    name = graphene.String(description='The name of the department')


class Employee(SQLAlchemyObjectType):
    class Meta(object):
        model = EmployeeModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee)
    department = relay.Node.Field(Department)


schema = graphene.Schema(query=Query)
