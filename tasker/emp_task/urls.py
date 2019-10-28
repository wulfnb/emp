from django.urls import path
from .views import employee_view
urlpatterns = [
    path('', employee_view,name='emp_dashboard'),
]
