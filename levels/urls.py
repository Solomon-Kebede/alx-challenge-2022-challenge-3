from django.urls import path
from . import views

urlpatterns = [
    path('level0/', views.level0, name='level0'),
]
