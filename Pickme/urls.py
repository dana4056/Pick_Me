from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('edit.html', views.edit, name='edit'),
    path('base.html', views.base, name='base'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
