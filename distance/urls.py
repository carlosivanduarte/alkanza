from django.urls import path

from . import views

app_name = 'distance'
urlpatterns = [
    path('', views.index, name='index'),
]