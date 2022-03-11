from django.db import models
from django.urls.base import reverse 

# Create your models here.
class Schedule(models.Model):
    time = models.DateTimeField()
    task = models.ForeignKey(
        'Task',
        on_delete = models.CASCADE,
    )
    amount = models.IntegerField()
    worker = models.CharField(max_length=150)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.task.task

    def get_absolute_url(self):
        return reverse ('sche_app:index')

class Task(models.Model):
    task = models.CharField(max_length=150)
    unit = models.CharField(max_length=150)
    point = models.IntegerField()

    def __str__(self):
        return self.task