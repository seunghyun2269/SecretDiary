from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.board, name = 'board'),
    path('create/', views.create, name = 'create'),
    path('diary/', views.diary, name = 'diary'),
    path('', views.main, name = 'main'),
]