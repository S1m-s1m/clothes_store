from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('clothes/', views.clothes_view.as_view(), name='clothes'),
    path('clothes/<slug:url>/', views.clothes_detail_view, name='clothes_detail'),
    path('season_clothes/<str:season>/', views.season_clothes, name='season_clothes'),
    path('review/', views.review_view, name='add_review'),
    path('add_cloth/', views.add_cloth_view, name='add_cloth')
]