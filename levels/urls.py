from django.urls import path
from . import views

urlpatterns = [
    path('level0', views.level0, name='level0'),
    path('level1', views.level1, name='level1'),

    # The following are to mock the error pages
    path('<str:url>', views.custom_404_view_1, name='error_404_1'),
    path('<str:url>/', views.custom_404_view_1, name='error_404_1'),
]
