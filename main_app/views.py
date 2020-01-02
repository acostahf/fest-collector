from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Festival, Rating, Toy
from .forms import RatingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def add_rating(request, festival_id):
    form = RatingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.festival_id = festival_id
        new_feeding.save()
    return redirect('detail', festival_id=festival_id)

@login_required
def assoc_toy(request, festival_id, toy_id):
    Festival.objects.get(id=festival_id).toys.add(toy_id)
    return redirect('detail', festival_id=festival_id)

@login_required
def unassoc_toy(request, festival_id, toy_id):
    Festival.objects.get(id=festival_id).toys.remove(toy_id)
    return redirect('detail', festival_id=festival_id)

class FestivalCreate(LoginRequiredMixin, CreateView):
    model = Festival
    fields = ['name', 'location', 'description', 'year']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class FestivalUpdate(LoginRequiredMixin, UpdateView):
    model = Festival
    fields = '__all__'

class FestivalDelete(LoginRequiredMixin, DeleteView):
    model = Festival
    success_url = '/festivals/'

def home(request):
    return HttpResponse('<h1>oh..Hello</h1>')


def about(request):
    return render(request, 'about.html')

@login_required
def festivals_index(request):
    festivals = Festival.objects.filter(user=request.user)
    return render(request, 'festivals/index.html', {'festivals': festivals})

@login_required
def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    toys_festival_doesnt_have = Toy.objects.exclude(id__in = festival.toys.all().values_list('id'))
    rating_form = RatingForm()
    return render(request, 'festivals/detail.html', { 'festival': festival, 'rating_form': rating_form, 'toys': toys_festival_doesnt_have })

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)