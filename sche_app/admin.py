from django.contrib import admin
from  .models import Schedule, Task

# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'worker', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'task')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'unit', 'point')
    list_display_links = ('id', 'task')



admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Task, TaskAdmin)

