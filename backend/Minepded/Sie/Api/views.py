from rest_framework.generics import ListAPIView

from .serializers import ThematiqueSerializer
from ..models import Thematique


class ThematiqueListView(ListAPIView):
    queryset = Thematique.objects.all()
    serializer_class = ThematiqueSerializer
