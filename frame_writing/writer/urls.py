from django.urls import path
from . import views

app_name = 'writer'
urlpatterns = [
    path('', views.index, name='index'),
]