import requests
from django.shortcuts import render

api_key = 'cc74cee4a73688e98909b2e1d59cbfd6'
latitude = 19.284691
longitude = 72.860687


def home(request):
    url = 'https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}'
    header = {
        'user-key': api_key
    }
    response = requests.get(url.format(latitude, longitude), headers=header).json()

    location = response['location']['title']
    restaurant_array = response['nearby_restaurants']
    length = len(restaurant_array)

    restaurants = []
    for i in range(0, length):
        restaurant_obj = restaurant_array[i]['restaurant']
        restaurant = {
            'id': restaurant_obj['id'],
            'name': restaurant_obj['name'],
            'locality': restaurant_obj['location']['locality'],
            'image': restaurant_obj['featured_image'],
            'cost': restaurant_obj['currency'] + str(restaurant_obj['average_cost_for_two'])
        }
        restaurants.append(restaurant)

    context = {
        'location': location,
        'restaurants': restaurants
    }

    return render(request, 'DJEats/home.html', context)


def details(request):
    return render(request, 'DJEats/details.html')
