from django.urls import path
from . import views

urlpatterns = [
    path('', views.getnotes, name="home"),
    path('note/<int:k>/', views.getnote),
    path(r'^logout$', views.user_logout, name='auth_logout')
]
