from django.urls import include, path
from composeexample.viewsets import AlbumViewSet, MusicianViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'musicians', MusicianViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]