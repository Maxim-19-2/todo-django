from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index.html'),
    path('', views.add_todo, name='add_todo.html'),
    path('', views.impressum, name='impressum.html'),
]