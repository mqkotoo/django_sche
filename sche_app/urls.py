from django.urls import path

from . import views

app_name = 'sche_app'

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='index'),
    path('new_sche', views.CreateView.as_view(), name='new_sche'),
    path('edit_sche/<int:pk>', views.UpdateView.as_view(), name='edit_sche'),
    path('delete_sche/<int:pk>', views.DeleteView.as_view(), name='delete_sche'),
    path('new_task', views.CreateTaskView.as_view(), name='new_task'),
    # 仕事情報の編集のパスを通す
    path('edit_task/<int:pk>', views.UpdateTaskView.as_view(), name='edit_task'),
    # タスクの内容を編集するためのパスを通す
    path('delete_task/<int:pk>', views.DeleteTaskView.as_view(), name='delete_task'),

]