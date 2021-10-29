from composeexample.models.album import Album
from composeexample.models.musician import Musician
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['artist', 'name', 'release_date', 'num_stars']

class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']
 