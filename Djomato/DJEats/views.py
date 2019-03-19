import requests
from django.shortcuts import render

api_key = 'cc74cee4a73688e98909b2e1d59cbfd6'
latitude = 19.284691
longitude = 72.860687


def home(request):
    url = 'https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}'
    header = {
        'user-key': 'cc74cee4a73688e98909b2e1d59cbfd6'
    }
    response = requests.get(url.format(latitude, longitude), headers=header)
    new_url = url.format(latitude, longitude)
    print(response.text)
    return render(request, 'DJEats/home.html')
