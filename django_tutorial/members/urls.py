from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.helloworld, name='members'),
]