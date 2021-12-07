from django.conf.urls import url
from django.urls import path, include
from . views import *


urlpatterns = [
    path('keyword/',KeywordView.as_view()),  # 키워드 리스트 추가, 조회 등 가능
    path('recommend/<str:user_id>', RecommendView.as_view()),  # 유저별 추천 리스트
    path('user/<str:user_id>', UserDetailView.as_view()),  # 유저의 상세정보
    path('founder/', FounderView.as_view()),  # 창업주 리스트
    path('factory/', FactoryView.as_view()),  # 공장주 리스트
    path('founder/estimate/', FounderEstView.as_view()),  # 견적서 리스트
    path('founder/estimate/<int:pk>/', FounderEstDetailView.as_view()),  # 견적서 상세정보
    path('factory/information/', FactoryInfoView.as_view()),  # 공장 소개 리스트
    path('factory/information/<int:pk>/', FactoryInfoDetailView.as_view()),  # 공장 상세정보
]