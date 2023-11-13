
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Task

# Create your views here.


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'task': tasks,
    }
    return render(request, 'todo/home.html', context)


def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")
