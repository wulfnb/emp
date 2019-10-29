from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
import json

# Create your views here.
@login_required
def employee_view(request):
    context = {}
    return render(request, "emp_task/emp.html", context)

def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('id'):
            tmp = Task.objects.get(pk=data.get('id'))
            print(tmp)
            tmp.status = data.get('status').lower()
        else:
            tmp = Task()
        tmp.task = data.get('name')
        tmp.employee = request.user
        tmp.save()
        return HttpResponse({"success": True})
    else:
        return HttpResponse({"failed": True})
