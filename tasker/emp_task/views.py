from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.
@login_required
def employee_view(request):
    context = {}
    return render(request, "emp_task/emp.html", context)

def add_task(request):
    if request.POST:
        tmp = Task()
        tmp.task = request.GET.get('name')
        return HttpResponse({"success": True})
    else:
        return HttpResponse({"failed": True})
