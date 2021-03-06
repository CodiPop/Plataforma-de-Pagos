"""Plataforma_de_pagos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pagos.views import *
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', inicio, name='index'),
    path('admin/', admin.site.urls),
    path('registrarse/', registrarse, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('tarjetas/',cards,name='tarjetas'),
    path('pse_registro/',creartarjetapse,name='tarjetaspse'),
    path('registrartarjeta/',creartarjeta,name='guardartarjeta'),
    path('registrarpago/',crearpago,name='guardarpago'),
    path('transacciones/',transacciones,name='vertransacciones'),
]

urlpatterns += staticfiles_urlpatterns()