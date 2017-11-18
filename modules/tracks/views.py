from rest_framework import viewsets, filters
from .models import Track
from . serializers import TrackModelSerializer, TrackAlbumSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class TrackViewSet(viewsets.ModelViewSet):

    # serializer_class = TrackAlbumSerializer
    serializer_class = TrackModelSerializer
    queryset = Track.objects.all().select_related('album')
    # con select_related mejoramos performance porque el query ya trae las relaciones de los albumes
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('rating', 'duration')
    search_fields = ('name', 'album_name')
    # permission_classes = (IsAuthenticated,)
