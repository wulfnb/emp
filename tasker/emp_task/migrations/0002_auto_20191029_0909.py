# Generated by Django 2.2.6 on 2019-10-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(choices=[('added', 'added'), ('inprogress', 'inprogress'), ('completed', 'completed')], default=True),
        ),
    ]
