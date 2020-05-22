from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jumbotron, name = "jumbotron"),
    path('carousel/', views.carousel, name = "carousel"),
    path('album/', views.album, name = "album"),
    path('sign-in/', views.signin, name = "sign-in"),
    path('registro/', views.registro, name = "registro"),
]
