from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm

def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, 'todoapp/show_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'todoapp/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    
    return render(request, 'todoapp/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.delete()
    return redirect('show_tasks')

def complete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'todoapp/completed_tasks.html', {'tasks': tasks})
