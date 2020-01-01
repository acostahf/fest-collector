from django.db import models

# Create your models here.
VIBES = (
    ('B', 'Bad'),
    ('G', 'Good'),
    ('P', 'Plur')
)


class Festival(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()


class Rating(models.Model):
    date = models.DateField()
    vibe = models.CharField(
        max_length=1,
        choices=VIBES,
        default=VIBES[0][0]
    )
