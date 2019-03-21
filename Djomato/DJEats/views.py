import requests
from django.http import HttpResponse
from django.shortcuts import render

api_key = 'cc74cee4a73688e98909b2e1d59cbfd6'
latitude = 19.284691
longitude = 72.860687


def home(request):
    return render(request, 'DJEats/home.html')


def details(request):
    return render(request, 'DJEats/details.html')
