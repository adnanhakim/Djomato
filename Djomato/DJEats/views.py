import requests
from django.http import HttpResponse
from django.shortcuts import render

api_key = 'cc74cee4a73688e98909b2e1d59cbfd6'
latitude = 19.284691
longitude = 72.860687


def home(request):
    url = 'https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}'
    header = {
        'user-key': api_key
    }
    response = requests.get(url.format(
        latitude, longitude), headers=header).json()

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
            'image': restaurant_obj['thumb'],
            'cost': restaurant_obj['currency'] + str(restaurant_obj['average_cost_for_two'])
        }
        restaurants.append(restaurant)

    context = {
        'location': location,
        'restaurants': restaurants
    }

    return render(request, 'DJEats/home.html', context)


def details(request, restaurant_id=0):

    is_restaurant = True
    if restaurant_id == 0:
        is_restaurant = False
        context = {
            'restaurant_id': restaurant_id,
            'is_restaurant': is_restaurant
        }

    else:
        url = 'https://developers.zomato.com/api/v2.1/restaurant?res_id={}'
        header = {
            'user-key': api_key
        }
        response = requests.get(url.format(
            restaurant_id), headers=header).json()

        restaurant = {
            'id': response['id'],
            'name': response['name'],
            'address': response['location']['address'],
            'featured_image': response['featured_image'],
            'avg_rating': int(round((float(response['user_rating']['aggregate_rating'])/5)*100, 2)),
            'avg_review': response['user_rating']['rating_text'],
            'no_of_votes': response['user_rating']['votes'],
            'rating_color': response['user_rating']['rating_color'],
            'cuisines': response['cuisines']
        }

        context = {
            'restaurant': restaurant,
            'is_restaurant': is_restaurant
        }

    if(restaurant_id == 0):
        return render(request, 'DJEats/test.html', context)
    else:
        return render(request, 'DJEats/test.html', context)
