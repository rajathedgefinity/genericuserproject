from django.urls import path,include
from allauthuserapp import api_urls

urlpatterns = [
    path('api/',include('allauthuserapp.api_urls')),
]
