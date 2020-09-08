from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('board/', views.board, name = 'board'),
    path('create/', views.create, name = 'create'),
    # /posts/5/ 
    path('<int:post_id>/', views.diarypage, name = 'diarypage'),
    # /posts/5/update
    # path('<int:post_id>/update', views.update, name='update'),
    # /posts/5/delete
    path('<int:post_id>/delete/', views.delete, name = 'delete'),
]