# Generated by Django 5.2 on 2025-05-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_actor_movies_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='actors',
            field=models.ManyToManyField(default='no one', related_name='acted_movie', to='movie_app.actor'),
        ),
    ]
