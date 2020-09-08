from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('board/', views.board, name = 'board'),
    path('create/', views.create, name = 'create'),
    # /posts/5/ 
    path('<int:pk>/', views.diarypage, name = 'diarypage'),
    # /posts/5/update
    path('<int:pk>/update', views.update, name='update'),
    # /posts/5/delete
    path('<int:pk>/delete/', views.delete, name = 'delete'),
]