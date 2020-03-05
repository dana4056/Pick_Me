from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('edit.html', views.edit, name='edit'),
    path('pickme.html', views.pickme, name='pickme')
]
