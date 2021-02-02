from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('first/list/', views.list, name='list'),
    path('first/create/', views.create, name='infectedplace-create'),
    path('first/ipserializer/', views.ipserializer, name='ipserializer'),
    path('first/update/', views.update, name='infectedplace-update'),
    path('first/detail/', views.detail, name='infectedplace-detail'),
    path('first/delete/', views.delete, name='infectedplace-delete'), 
]