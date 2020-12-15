from rest_framework.generics import ListAPIView

from .serializers import *
from ..models import *


class ThematiqueListView(ListAPIView):
    queryset = Thematique.objects.all()
    serializer_class = ThematiqueSerializer


class ProjetListView(ListAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer


class ProgrammeListView(ListAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer


class IndicateurListView(ListAPIView):
    queryset = Indicateur.objects.all()
    serializer_class = IndicateurSerializer


class CategorieMesureListView(ListAPIView):
    queryset = CategorieMesure.objects.all()
    serializer_class = IndicateurSerializer


class MesureListView(ListAPIView):
    queryset = Mesure.objects.all()
    serializer_class = MesureSerializer
