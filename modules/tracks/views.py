from rest_framework import viewsets
from .models import Track
from . serializers import TrackModelSerializer, TrackAlbumSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TrackViewSet(viewsets.ModelViewSet):

    # serializer_class = TrackAlbumSerializer
    serializer_class = TrackModelSerializer
    queryset = Track.objects.all().select_related('album')
    # con select_related mejoramos performance porque el query ya trae las relaciones de los albumes
    permission_classes = (IsAuthenticated,)
