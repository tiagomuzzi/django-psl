from django.contrib.auth.models import User
from rest_framework import serializers

from composeexample.models.album import Album
from composeexample.models.musician import Musician
from composeexample.models.track import Track


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['artist', 'name', 'release_date', 'num_stars']


class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ['title', 'length']
