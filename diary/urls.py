from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.board, name = 'board'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>/', views.diary, name = 'diary'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('', views.main, name = 'main'),
]