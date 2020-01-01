from django.shortcuts import render
from django.http import HttpResponse
from .models import Festival


# class Festival:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, location, description, year):
#         self.name = name
#         self.location = location
#         self.description = description
#         self.year = year


festivals = [
    Festival('ACL', 'Austin', '3day two weekend', 2019),
    Festival('EDC', 'Las Vegas', 'Ravers everywhere', 2018),
    Festival('Electric Forest', 'Michigan',
             'the forest becomes a huge rave', 2016)
]

# Create your views here.


def home(request):
    return HttpResponse('<h1>oh..Hello</h1>')


def about(request):
    return render(request, 'about.html')


def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/index.html', {'festivals': festivals})

def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    return render(request, 'festivals/detail.html', { 'festival': festival })