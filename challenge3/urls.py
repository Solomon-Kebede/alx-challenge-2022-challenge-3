"""
URL configuration for challenge3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render
from django.shortcuts import redirect

def custom_404_view_2(request, url):
    return render(request, '404/404.html', status=404)

def projects_view(request):
    return render(request, 'projects/100018.html')

def index(request):
    return redirect('projects/100018')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home_page'),
    path('ch4ll3n632022/', include('levels.urls')),
    path('projects/100018', projects_view, name='projects'),
    # The following are to mock the error pages
    path('<str:url>', custom_404_view_2, name='match_url'),
    path('<str:url>/', custom_404_view_2, name='match_url'),
]
