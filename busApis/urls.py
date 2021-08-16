from django.urls import path
from busApis import views

urlpatterns = [

    path('', views.home, name='home'),
]
