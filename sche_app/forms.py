from django import forms
from django.forms import fields
from . models import Schedule, Task

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'time': forms.SelectDateWidget
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'