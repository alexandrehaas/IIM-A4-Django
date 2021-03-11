"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('blockchain-team', views.blockchainTeam, name='blockchainTeam'),
    path('databases-team', views.databasesTeam, name='databasesTeam'),
    path('graphic-team', views.graphicTeam, name='graphicTeam'),
    path('ia-team', views.IATeam, name='IATeam'),
    path('objects-team', views.objectsTeam, name='objectsTeam'),
    path('softwares-team', views.softwaresTeam, name='softwaresTeam'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cv', views.cv, name='cv'),
]
