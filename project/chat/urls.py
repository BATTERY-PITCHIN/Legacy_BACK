from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.search, name='search'),
    path('<str:room_name>/', views.room, name='room'),
]