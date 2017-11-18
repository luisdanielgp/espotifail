from django.shortcuts import render
from rest_framework.views import APIView
# con esto creamos vistas a partir de clases en vez de funciones
from rest_framework import status
# http statuses
from rest_framework.response import Response
# el serializer nos da un dict y Response lo convierte a json
from .models import Artist
from .serializers import ArtistsModelSerializer
from django.http import Http404
from django.db.models import Q


# Create your views here.


class ListArtist(APIView):  # por convención, list artist lista a todos los artistas
    '''
    Este endpoint trae todos los artistas
    '''

    def _filtering(self, params):
        genre = params.get('genre', "")
        band = params.get('band', False)
        name = params.get('name', "")
        # con el get, si no encuentra nos trae el segundo elemento del parentesis

        queryset = Artist.objects.filter(Q(primary_genre__iexact=genre) & Q(
            is_band=band) & Q(name__icontains=name))

        return queryset

    def get(self, request):

        if request.query_params:
            query = self._filtering(request.query_params)
            serializer = ArtistsModelSerializer(query, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            artists = Artist.objects.all()  # obtenemos todos los artistas de la bdd
            serializer = ArtistsModelSerializer(artists, many=True)
            # convertimos los diccionarios obtenidos en lista tipo json
            #  con el many=True trae una lista de diccionarios
            #  sin el many nos trae un diccionario
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistsModelSerializer(data=request.data)
        if serializer.is_valid():  # is_valid regrea true si la data que me mandaron es válida
            serializer.save()  # save guarda directo en la bdd
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # se vuelve a llamar serializer.data porque ahora ya tiene id en la bdd
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailArtist(APIView):  # por convención detail modifica un artista específico

    def _get_artist(self, id):
        try:
            artist = Artist.objects.get(id=id)
            return artist
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistsModelSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistsModelSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistsModelSerializer(
            artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = self._get_artist(id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
