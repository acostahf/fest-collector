from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
VIBES = (
    ('B', 'Bad'),
    ('G', 'Good'),
    ('P', 'Plur')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})



class Festival(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'festival_id': self.id})


class Rating(models.Model):
    date = models.DateField('rating date')
    vibe = models.CharField(
        max_length=1,
            choices=VIBES,
            default=VIBES[0][0]
    )
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_vibe_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

