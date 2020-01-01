from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('about/', views.about, name='about'),
    path('festivals/', views.festivals_index, name='index'),
    path('festivals/<int:festival_id>/', views.festivals_detail, name='detail'),
]
