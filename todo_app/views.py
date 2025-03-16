from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    form=TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request,'todo_app/task_list.html',{'tasks':tasks,'form':form})
    
def delete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def update_task(request,task_id):
    task = Task.objects.get(id=task_id)
    form=TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
          form.save()
        return redirect('task_list')
    return render(request,'todo_app/update_task.html',{'form':form})
    
