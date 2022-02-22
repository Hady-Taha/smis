from django.urls import path
from . import views

urlpatterns = [
    path('professor', views.professor, name="professor"),
]
