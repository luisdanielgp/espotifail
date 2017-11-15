from django.shortcuts import render
from rest_framework import generics  # generics sustituye APIView, Response y status
from .models import Album
from .serializers import AlbumModelSerializer, AlbumTracksSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import GroupAPermissions

# Create your views here.


# generics nos da un crud generico con APIView, sin embargo solo se puede usar con ModelSerializer
class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumTracksSerializer
    permission_classes = (IsAuthenticated, GroupAPermissions)


class DetailGenericAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
