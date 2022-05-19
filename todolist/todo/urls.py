from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index.html'),
    path('edit_todo.html', views.edit_todo, name='edit_todo.html'),
    path('add_todo.html', views.add_todo, name='add_todo.html'),
    path('impressum.html', views.impressum, name='impressum.html'),
    path('delete/<str:toDelete>', views.delete, name='delete'),
    path('edit/<str:toEdit>', views.edit, name='edit'),
    path('update/<str:toBeUpdated>', views.update, name='update'),
]