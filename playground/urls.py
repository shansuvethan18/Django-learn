from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
     path('hello/hellow', views.say_hellow,name="home")
]