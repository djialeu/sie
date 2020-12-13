from rest_framework import serializers

from ..models import Thematique


class ThematiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thematique
        fields = ('id', 'name')
