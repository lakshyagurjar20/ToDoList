from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'todo/task_list.html', {'tasks': tasks})
