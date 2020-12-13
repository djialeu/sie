from django.urls import path

from .views import ThematiqueListView

urlpatterns = [
    path('', ThematiqueListView.as_view())
]
