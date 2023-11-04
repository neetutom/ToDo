from django.shortcuts import render, redirect

from .forms import todoForm
from .models import Task


# Create your views here.
def Home(request):
    return render(request, 'base.html')


def add_task(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'addTask.html', {'task': tasks})



def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = todoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'task':task})
