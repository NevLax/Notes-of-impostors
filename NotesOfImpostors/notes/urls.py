from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('notes/', views.getNotes),
    path('note/<int:k>/', views.getNote),
]