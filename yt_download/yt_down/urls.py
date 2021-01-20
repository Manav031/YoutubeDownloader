from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.yt_main, name='home'),
    path('download', views.yt_download),
    path('download_cmpt/<res>', views.compt, name='download_cmpt')
]