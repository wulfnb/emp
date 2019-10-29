import graphene
from graphene_django.types import DjangoObjectType
from .models import Task, User


class TaskGrp(DjangoObjectType):
    class Meta:
        model = Task

class UserGrp(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    all_tasks = graphene.List(TaskGrp)
    all_user = graphene.List(UserGrp)

    employee = graphene.Field(UserGrp, 
                          id=graphene.Int(),
                          username=graphene.String())
    task = graphene.Field(TaskGrp, 
                          id=graphene.Int())

    def resolve_all_tasks(self, info, **kwargs):
        return Task.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return User.objects.select_related('task').all()
        # return User.object.all()

    def resolve_task(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Task.objects.get(pk=id)

        return None

    def resolve_employee(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
            return User.objects.get(pk=id)

        if username is not None:
            return User.objects.get(username=username)
        return None

class Query2(Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query2)