from django.conf.urls import url
from django.urls import path, include
from . views import *


urlpatterns = [
    path('keyword/',KeywordView.as_view()),
    path('recommend/<str:user_id>', RecommendView.as_view()),
    path('founder/', FounderView.as_view()),
    path('factory/', FactoryView.as_view()),
    path('founder_estimate/', FounderEstView.as_view()),
    path('factory_information/', FactoryInfoView.as_view()),
]