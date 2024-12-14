from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("todos/",views.todos, name="todos"),
    path("sathi/",views.sathi, name="sathi"),
    path("modelui/",views.modelui, name="modelui"),
    path('transcribe/',views.transcribe, name='transcribe'),
]