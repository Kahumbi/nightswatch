from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hood-home'),
    path('about/', views.about, name='hood-about'),
]