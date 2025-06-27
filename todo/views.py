from django.shortcuts import render
from .models import Task

def task_list(request):
    query = request.GET.get('q')  # get 'q' param from URL
    tasks = Task.objects.all().order_by('-created')
    if query:
        tasks = tasks.filter(title__icontains=query)
    return render(request, 'todo/task_list.html', {'tasks': tasks, 'query': query})


from django.shortcuts import redirect
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

from django.shortcuts import get_object_or_404

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/update_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/delete_task.html', {'task': task})
