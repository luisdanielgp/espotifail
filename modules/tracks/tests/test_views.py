import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from modules.tracks.models import Track
from modules.tracks.models import Album
from modules.tracks.serializers import TrackModelSerializer


class TestGetAllTracks(TestCase):
    client = Client()

    def setUp(self):
        album = Album.objects.create(name="el nuevo album", cover="http://google.com", release_day="2017-01-01",
                                     copyright="derechos", genre="rock", track_count="12", country="MX", price="12.5", currency="MX")
        track1 = Track.objects.create(name="Track1", duration=123,
                                      url_youtube="http://youtube.com/", album=album, rating=4.2)
        track2 = Track.objects.create(name="Track2", duration=321,
                                      url_youtube="http://youtube.com/", album=album, rating=2.4)

    def test_all_tracks(self):
        response = self.client.get(reverse("tracks:tracksViewset-list"))
        # tracks es el namespace en las urls generales, trackViewSet es el base_name en las urls de tracks
        tracks = Track.objects.all()
        serializer = TrackModelSerializer(tracks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class TestCreateTracks(TestCase):
    client = Client()

    def setUp(self):
        self.album = Album.objects.create(name="el nuevo album", cover="http://google.com", release_day="2017-01-01",
                                          copyright="derechos", genre="rock", track_count="12", country="MX", price="12.5", currency="MX")
        self.valid_track = {"name": "Track1", "duration": 123,
                            "url_youtube": "http://youtube.com/", "album": str(self.album.id), "rating": 4.2}
        self.invalid_track = {"name": "Track2", "duration": -321,
                              "url_youtube": "youtube", "album": str(self.album.id), "rating": 2.4}

    def test_create_valid_tracks(self):
        response = self.client.post(reverse(
            "tracks:tracksViewset-list"), data=json.dumps(self.valid_track), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_tracks(self):
        response = self.client.post(reverse(
            "tracks:tracksViewset-list"), data=json.dumps(self.invalid_track), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestGetSingleTrack(TestCase):
    client = Client()

    def setUp(self):
        album = Album.objects.create(name="el nuevo album", cover="http://google.com", release_day="2017-01-01",
                                          copyright="derechos", genre="rock", track_count="12", country="MX", price="12.5", currency="MX")
        self.track1 = Track.objects.create(name="Track1", duration=123,
                                           url_youtube="http://youtube.com/", album=album, rating=4.2)

    def test_get_valid_tracks(self):
        response = self.client.get(reverse("tracks:tracksViewset-detail",
                                           kwargs={'pk': str(self.track1.id)}))
        tracks = Track.objects.get(pk=self.track1.id)
        serializer = TrackModelSerializer(tracks)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_tracks(self):
        response = self.client.get(reverse("tracks:tracksViewset-detail",
                                           kwargs={'pk': 'jnfernrv5reeruin'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestModifyTracks(TestCase):
    client = Client()

    def setUp(self):
        self.album = Album.objects.create(name="el nuevo album", cover="http://google.com", release_day="2017-01-01",
                                          copyright="derechos", genre="rock", track_count="12", country="MX", price="12.5", currency="MX")
        self.track1 = Track.objects.create(name="Track1", duration=123,
                                           url_youtube="http://youtube.com/", album=self.album, rating=4.2)
        self.valid_track = {"name": "Track1", "duration": 123,
                            "url_youtube": "http://youtube.com/", "album": str(self.album.id), "rating": 4.2}
        self.invalid_track = {"name": "Track2", "duration": -321,
                              "url_youtube": "youtube", "album": str(self.album.id), "rating": 2.4}

    def test_modify_valid_tracks(self):
        response = self.client.put(reverse("tracks:tracksViewset-detail",
                                           kwargs={'pk': str(self.track1.id)}), data=json.dumps(self.valid_track), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_modify_invalid_tracks(self):
        response = self.client.put(reverse("tracks:tracksViewset-detail",
                                           kwargs={'pk': str(self.track1.id)}), data=json.dumps(self.invalid_track), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestDeleteTrack(TestCase):
    client = Client()

    def setUp(self):
        self.album = Album.objects.create(name="El nuevo album",
                                          cover="http://google.com",
                                          release_day="2017-01-01",
                                          copyright="derechos",
                                          genre="rock",
                                          track_count=12,
                                          country="MX",
                                          price=12.5,
                                          currency="MX"
                                          )

        self.track1 = Track.objects.create(
            name="Track1",
            duration=123,
            url_youtube="http://youtube.com/",
            album=self.album,
            rating=4.2
        )

    def test_delete_track(self):
        response = self.client.delete(reverse("tracks:tracksViewset-detail",
                                              kwargs={"pk": str(self.track1.id)}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
