# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('photo', models.URLField()),
                ('is_band', models.BooleanField(default=False)),
                ('primary_genre', models.CharField(choices=[('POP', 'Pop'), ('ROCK', 'Rock'), ('ELT', 'Electronic'), ('JAZZ', 'Jazz'), ('CLS', 'Classic'), ('LTN', 'Latino'), ('RAP', 'Rap'), ('R&B', 'R&B'), ('FLK', 'Folk'), ('OT', 'Other')], max_length=100)),
                ('albums', models.ManyToManyField(to='albums.Album')),
            ],
        ),
    ]
