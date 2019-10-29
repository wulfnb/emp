from django.urls import path
from .views import employee_view, add_task
from graphene_django.views import GraphQLView

from .schema import schema


urlpatterns = [
    path('', employee_view, name='emp_dashboard'),
    path('add_task', add_task, name='add_task'),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
