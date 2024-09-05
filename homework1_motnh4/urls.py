"""
URL configuration for homework1_motnh4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from myapp.views import text_response, html_response

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('text/', text_response, name='text_response'),  # API с текстовым ответом
    path('html/', html_response, name='html_response'),  # API с HTML-ответом
]
