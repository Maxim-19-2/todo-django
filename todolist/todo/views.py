import re
from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def add_todo(req):
    return render(req, 'add_todo.html')

def impressum(req):
    return render(req, 'impressum.html')