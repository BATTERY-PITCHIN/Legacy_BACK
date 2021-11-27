from django.conf.urls import url
from django.urls import path, include
from . views import *


urlpatterns = [
    path('founder/', FounderView.as_view(), name='index'),
    path('factory/', FactoryView.as_view(), name='index'),
]