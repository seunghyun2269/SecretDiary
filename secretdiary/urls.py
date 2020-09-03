from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from diary import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board', views.board, name="borad.html"),
    path('diarypage', views.diarypage, name="diarypage.html")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("accounts.urls")), 
    path('diary/', include("diary.urls")), 
]
>>>>>>> 58d59258a8195ed83c69d40164ce88191bfb71be
