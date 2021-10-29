from rest_framework import viewsets

from composeexample.models.musician import Musician
from composeexample.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
