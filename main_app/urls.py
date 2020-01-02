from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('about/', views.about, name='about'),
    path('festivals/', views.festivals_index, name='index'),
    path('festivals/<int:festival_id>/', views.festivals_detail, name='detail'),
    path('festivals/create/', views.FestivalCreate.as_view(), name='festivals_create'),
    path('festivals/<int:pk>/update/', views.FestivalUpdate.as_view(), name='festivals_update'),
    path('festivals/<int:pk>/delete/', views.FestivalDelete.as_view(), name='festivals_delete'),
    path('festivals/<int:festival_id>/add_rating/', views.add_rating, name='add_rating'),
]
