from rest_framework import viewsets

from composeexample.models.track import Track
from composeexample.serializers import TrackSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
