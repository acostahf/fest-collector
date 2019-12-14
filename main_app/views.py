from django.shortcuts import render
from django.http import HttpResponse


class Festival:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, location, description, year):
        self.name = name
        self.location = location
        self.description = description
        self.year = year


festivals = [
    Festival('Lolo', 'tabby', 'foul little demon', 3),
    Festival('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Festival('Raven', 'black tripod', '3 legged cat', 4)
]

# Create your views here.


def home(request):
    return HttpResponse('<h1>oh..Hello</h1>')


def about(request):
    return render(request, 'about.html')


def festivals_index(request):
    return render(request, '/festivals.index.html', {'festivals': festivals})
