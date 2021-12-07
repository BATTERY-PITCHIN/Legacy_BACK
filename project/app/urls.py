from django.conf.urls import url
from django.urls import path, include
from . views import *


urlpatterns = [
    path('keyword/',KeywordView.as_view()),
    path('recommend/<str:user_id>', RecommendView.as_view()),
    path('founder/', FounderView.as_view()),
    path('factory/', FactoryView.as_view()),
    path('founder/estimate/', FounderEstView.as_view()),
    path('founder/estimate/<int:est_id>/', FounderEstView.as_view()),
    path('factory/information/', FactoryInfoView.as_view()),
    path('factory/information/<int:info_id>/', FactoryInfoView.as_view()),
]