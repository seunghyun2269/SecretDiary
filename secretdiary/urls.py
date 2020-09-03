from django.contrib import admin
from django.urls import path, include
from diary import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board', views.board, name="borad.html"),
    path('diarypage', views.diarypage, name="diarypage.html"),
    path('auth/', include("accounts.urls")), 
    path('diary/', include("diary.urls")), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
