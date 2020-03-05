from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('edit.html', views.edit, name='edit'),
    path('how_to_use.html', views.how_to_use, name='how_to_use'),
    path('team.html', views.team, name='team')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
