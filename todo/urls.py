from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-task/", views.add_task, name="add-task"),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark-as-done'),
    path("mark_as_undone/<int:pk>/", views.mark_as_undone, name='mark-as-undone'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit-task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete-task')

]
