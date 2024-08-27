from django.urls import path
from . import views

urlpatterns = [
    path('', views.getnotes, name="index"),
    path('note/<int:k>/', views.getnote),
]
