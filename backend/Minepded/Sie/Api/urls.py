from django.urls import path

from .views import *

urlpatterns = [
    path('thematiques', ThematiqueListView.as_view()),
    path('projets', ProjetListView.as_view()),
    path('programmes', ProgrammeListView.as_view()),
    path('categories_mesures', CategorieMesureListView.as_view()),
    path('mesures', MesureListView.as_view()),
    path('indicateurs', IndicateurListView.as_view()),
]
