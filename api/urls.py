from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/<str:pk>/', views.get_task, name="get_task"),
    path('tasks/new/', views.add_task, name="add_task"),
    path('tasks/update/<str:pk>/', views.update_task, name="update_task"),
    path('tasks/delete/<str:pk>/', views.delete_task, name="delete_task"),
]