from django.urls import path
from .views import employee_view
from graphene_django.views import GraphQLView

from .schema import schema


urlpatterns = [
    path('', employee_view,name='emp_dashboard'),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
