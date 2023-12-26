from django.urls import path
from . import views

urlpatterns = [
    path('level0', views.level0, name='level0'),
    path('level1', views.level1, name='level1'),
]
