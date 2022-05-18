import re
from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from todo.models import Todo
from django.views import View

# Create your views here.
def index(request):
    t=Todo(0, "funktioniert", "19. Mai 2022", 60)
    t.save()
    t2=Todo(1, "HA2 erledigen", "11. Mai 2022", 30)
    t2.save()

    todos = Todo.objects.all()
    t = loader.get_template('index.html')
    c = dict({'todos': todos})
    return HttpResponse(t.render(c))

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        print("hier")
        #return HttpResponse(result)

def edit_todo(req):
    return render(req, 'edit_todo.html')

def add_todo(req):
    return render(req, 'add_todo.html')

def impressum(req):
    return render(req, 'impressum.html')

#def delete(request, pk):
#    todo = Todo.objects.get(id=pk)
#    todo.delete()
#    return redirect('/')