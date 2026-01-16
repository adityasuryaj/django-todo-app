from django.shortcuts import render,get_object_or_404,redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        
    context = {
        'todos':todos,
        'form':form,
    }
    return render(request, 'todo/todo_list.html',context)

def todo_update(request,pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/todo_form.html',{'form':form,'todo':todo})

def todo_delete(request,pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request,'todo/todo_confirm_delete.html',{'todo':todo})

