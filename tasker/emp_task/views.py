from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def employee_view(request):
    context = {}
    return render(request, "emp_task/emp.html", context)
