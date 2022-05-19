import re

from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from todo.models import Todo
from django.views import View

# Create your views here.
def index(request):
    if request.method == 'POST':
        newTODO = Todo(
            title = request.POST['title'],
            date = request.POST['date'],
            progress = request.POST['progress']
        )
        newTODO.save()
        return redirect('/')

    todos = Todo.objects.all()
    t = loader.get_template('index.html')
    c = dict({'todos': todos})
    return HttpResponse(t.render(c))

def edit_todo(request):
    return render(request, 'edit_todo.html')

def add_todo(request):
    return render(request, 'add_todo.html')


def impressum(request):
    return render(request, 'impressum.html')

def delete(request, toDelete):
    todo = Todo.objects.get(id=toDelete)
    todo.delete()
    return redirect('/')

def edit(request, toEdit):
    findTodo = Todo.objects.get(id=toEdit)
    c = dict({'todo':findTodo})
    return render(request, 'edit_todo.html', c)

def update(request, toBeUpdated):
    todo = Todo.objects.get(id=toBeUpdated)
    todo.title = request.POST['title']
    todo.date = request.POST['date']
    todo.progress = request.POST['progress']
    todo.save()
    return redirect('/')