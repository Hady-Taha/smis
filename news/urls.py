from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about, name="about"),
    path('brigadier', views.brigadier, name="brigadier"),
    path('post/<int:id>', views.post_details, name="post_details"),
]

