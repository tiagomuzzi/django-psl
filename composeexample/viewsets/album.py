from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from composeexample.models.album import Album
from composeexample.serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=False)
    def most_recent_releases(self, request):
        recent_albums = Album.objects.all().order_by('-release_date')

        page = self.paginate_queryset(recent_albums)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_albums, many=True)
        return Response(serializer.data)
