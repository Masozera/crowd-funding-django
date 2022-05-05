from django.urls import include, path
from django.contrib import admin
from . import views


app_name = 'home'


urlpatterns = [
    path('', views.index, name='home'),
    path('home/category/<int:categoty_id>', views.category, name='category')
]
