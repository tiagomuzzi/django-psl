from composeexample.models.album import Album
from composeexample.models.musician import Musician
from composeexample.serializers import AlbumSerializer, MusicianSerializer
from rest_framework import viewsets

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Album.objects.all().order_by('-release_date')
    serializer_class = AlbumSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer