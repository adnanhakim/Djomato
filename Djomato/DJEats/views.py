import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

api_key = 'cc74cee4a73688e98909b2e1d59cbfd6'
google_maps_api_key = 'AIzaSyBnJKp9cv96UswwdTKcLf4nImfuxki__zI'
latitude = 19.284691
longitude = 72.860687


def home(request, lat='19.284691', lng='72.860687'):
    url = 'https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}'
    header = {
        'user-key': api_key
    }
    response = requests.get(url.format(
        lat, lng), headers=header).json()

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


@login_required
def details(request, restaurant_id=0):

    is_restaurant = True
    if restaurant_id == 0:
        is_restaurant = False
        context = {
            'restaurant_id': restaurant_id,
            'is_restaurant': is_restaurant
        }

    else:
        detail_url = 'https://developers.zomato.com/api/v2.1/restaurant?res_id={}'
        review_url = 'https://developers.zomato.com/api/v2.1/reviews?res_id={}'
        header = {
            'user-key': api_key
        }

        detail_response = requests.get(detail_url.format(
            restaurant_id), headers=header).json()

        restaurant = {
            'id': detail_response['id'],
            'name': detail_response['name'],
            'address': detail_response['location']['address'],
            'featured_image': detail_response['featured_image'],
            'avg_rating': int(round((float(detail_response['user_rating']['aggregate_rating'])/5)*100, 2)),
            'avg_review': detail_response['user_rating']['rating_text'],
            'no_of_votes': detail_response['user_rating']['votes'],
            'rating_color': detail_response['user_rating']['rating_color'],
            'cuisines': detail_response['cuisines']
        }

        review_response = requests.get(review_url.format(
            restaurant_id), headers=header).json()

        review_array = review_response['user_reviews']
        length = len(review_array)
        reviews = []

        for i in range(0, length):
            review_obj = review_array[i]['review']
            review = {
                'user_name': review_obj['user']['name'],
                'profile_image': review_obj['user']['profile_image'],
                'foodie_level': review_obj['user']['foodie_level'],
                'foodie_color': review_obj['user']['foodie_color'],
                'timestamp': review_obj['review_time_friendly'],
                'review_text': review_obj['review_text'],
                'rating': review_obj['rating'],
                'rating_text': review_obj['rating_text'],
                'rating_color': review_obj['rating_color']
            }
            reviews.append(review)

        context = {
            'restaurant': restaurant,
            'reviews': reviews,
            'is_restaurant': is_restaurant
        }

    if(restaurant_id == 0):
        return render(request, 'DJEats/test.html', context)
    else:
        return render(request, 'DJEats/test.html', context)


def profile(request):
    return render(request, 'DJEats/profile.html')
    