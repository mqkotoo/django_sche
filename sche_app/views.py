from sche_app.forms import ScheduleForm, TaskForm
from django.shortcuts import render
from django.views import generic
from .models import Schedule, Task
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'app/index.html')

class IndexView(generic.ListView):
    model = Schedule
    template_name = 'app/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(generic.ListView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': Task.objects.all()
        })
        return context

    def get_queryset(self):
        return Schedule.objects.all().order_by('-time')


class CreateView(generic.CreateView):
    form_class = ScheduleForm
    template_name = 'app/new_sche.html'

class UpdateView(generic.UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'app/edit_sche.html'

class DeleteView(generic.edit.DeleteView):
    model = Schedule
    success_url = reverse_lazy('sche_app:index')
    template_name = 'app/delete.html'

class CreateTaskView(generic.CreateView):
    model = Task
    success_url = reverse_lazy('sche_app:index')
    fields = ['task','unit','point']
    template_name = 'app/new_task.html'

class UpdateTaskView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'app/edit_task.html'
    success_url = reverse_lazy('sche_app:index')
    # fields = ['task','unit','point']

class DeleteTaskView(generic.DeleteView):
    model = Task
    # form_class = TaskForm
    template_name = 'app/delete_task.html'
    success_url = reverse_lazy('sche_app:index')


