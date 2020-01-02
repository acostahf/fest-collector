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
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('festivals/<int:festival_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('festivals/<int:festival_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('accounts/signup/', views.signup, name='signup'),
]
