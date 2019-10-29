from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_TYPES = (
    ('added', 'Added'),
    ('inprogress', 'Inprogress'),
    ('completed', 'Completed'),
)

class Task(models.Model):
    task = models.CharField(max_length = 255, blank = True, null = True)
    description = models.CharField(max_length = 500, blank = True, null = True)
    status = models.CharField(max_length = 15, choices=STATUS_TYPES)
    employee = models.ForeignKey(User,on_delete=None)
    added_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.task)
