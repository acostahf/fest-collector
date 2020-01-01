from django.db import models
from django.urls import reverse

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


    def __str__(self):
        return self.name
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'festival_id': self.id})


class Rating(models.Model):
    date = models.DateField()
    vibe = models.CharField(
        max_length=1,
        choices=VIBES,
        default=VIBES[0][0]
    )
