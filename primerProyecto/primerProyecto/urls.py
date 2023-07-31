from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("book_list/", views.book_list, name="book_list"),
    path("book_register/", views.book_register, name="book_register"),
    path("book_created/", views.book_created, name="book_created"),
    path('book_deleted/', views.book_deleted, name='book_deleted'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
