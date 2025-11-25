from django.urls import path
from . import views

#  URLs de home
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
]