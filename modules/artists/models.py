from django.db import models
import uuid  # evitamos los id's consecutivos que genera el autoFill
from modules.albums.models import Album  # aún no lo creamos pero tenemos que importarlo.

# Create your models here.

GENRE = (
    ('POP', 'Pop'),
    ('ROCK', 'Rock'),
    ('ELT', 'Electronic'),
    ('JAZZ', 'Jazz'),
    ('CLS', 'Classic'),
    ('LTN', 'Latino'),
    ('RAP', 'Rap'),
    ('R&B', 'R&B'),
    ('FLK', 'Folk'),
    ('OT', 'Other')
)


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.URLField()
    # con este manejamos la relación (muchos a muchos)
    albums = models.ManyToManyField(Album, blank=True)
    # blank = True nos deja crear el artista sin album
    is_band = models.BooleanField(default=False)
    primary_genre = models.CharField(max_length=100, choices=GENRE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return
