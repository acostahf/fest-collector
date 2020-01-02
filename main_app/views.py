from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Festival, Rating
from .forms import RatingForm

# class Festival:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, location, description, year):
#         self.name = name
#         self.location = location
#         self.description = description
#         self.year = year

# Create your views here.
def add_rating(request, festival_id):
    form = RatingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.festival_id = festival_id
        new_feeding.save()
    return redirect('detail', festival_id=festival_id)

class FestivalCreate(CreateView):
    model = Festival
    fields = '__all__'
    success_url = '/festivals/'

class FestivalUpdate(UpdateView):
    model = Festival
    fields = '__all__'

class FestivalDelete(DeleteView):
    model = Festival
    success_url = '/festivals/'

def home(request):
    return HttpResponse('<h1>oh..Hello</h1>')


def about(request):
    return render(request, 'about.html')


def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/index.html', {'festivals': festivals})

def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    rating_form = RatingForm()
    return render(request, 'festivals/detail.html', { 'festival': festival, 'rating_form': rating_form })