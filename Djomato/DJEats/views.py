import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RestaurantForm

api_key = 'cc74cee4a73688e98909b2e1d59cbfd6'
temp_api = 'AIzaSyDxf4re_Jtg62K09OUJ7Bp_WNYF7NDSXgE'
google_static_map_api = 'AIzaSyAt7g-OcW0k9qcG-75Yj3GrLGwLC2dRV3Q'
google_static_map_signature = 'ozeiYbY0r4vZO_a3EQCgSzuNHVM='
stolen_api = 'AIzaSyDqIj_SXTf5Z5DgE_cvn5VF9h5NbuaiCbs'
google_maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
temp_url = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Naya%20Nagar&key={}'
google_maps_api_key = 'AIzaSyDxf4re_Jtg62K09OUJ7Bp_WNYF7NDSXgE'
latitude = 19.284691
longitude = 72.860687


def home(request, lat='19.107022', lng='72.837201'):

    url = 'https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}'
    header = {
        'user-key': api_key
    }

    if 'search' in request.GET:
        search_query = request.GET['search']
        if search_query != '':
            print(search_query)
            google_maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={}&key={}'
            geocoding_result = requests.get(
                google_maps_url.format(search_query, temp_api)).json()
            if geocoding_result['status'] == 'OK':
                lat = geocoding_result['results'][0]['geometry']['location']['lat']
                lng = geocoding_result['results'][0]['geometry']['location']['lng']
                print(lat)
                print(lng)
            else:
                print(geocoding_result['error_message'])

        else:
            print('Empty')

    response = requests.get(url.format(lat, lng), headers=header).json()

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

        lat = detail_response['location']['latitude']
        lng = detail_response['location']['longitude']

        has_online_delivery_var = detail_response['has_online_delivery']
        if has_online_delivery_var == 1:
            has_online_delivery = 'Yes'
        else:
            has_online_delivery = 'No'

        has_reservation_var = detail_response['is_zomato_book_res']
        if has_reservation_var == 1:
            has_reservation = 'Yes'
        else:
            has_reservation = 'No'

        has_bogo_offers_var = detail_response['include_bogo_offers']
        if has_bogo_offers_var == True:
            has_bogo_offers = 'Yes'
        else:
            has_bogo_offers = 'No'

        if (float(detail_response['user_rating']['aggregate_rating'])/5)*100 < 90:
            rating_color = detail_response['user_rating']['rating_color']
        else:
            rating_color = '13FF00'


        restaurant = {
            'id': detail_response['id'],
            'name': detail_response['name'],
            'address': detail_response['location']['address'],
            'locality': detail_response['location']['locality_verbose'],
            'featured_image': detail_response['featured_image'],
            'avg_rating': int(round((float(detail_response['user_rating']['aggregate_rating'])/5)*100, 2)),
            'avg_review': detail_response['user_rating']['rating_text'],
            'no_of_votes': detail_response['user_rating']['votes'],
            'rating_color': rating_color,
            'cuisines': detail_response['cuisines'],
            'avg_cost_for_two': detail_response['currency'] + str(detail_response['average_cost_for_two']),
            'has_online_delivery': has_online_delivery,
            'has_reservation': has_reservation,
            'has_bogo_offers': has_bogo_offers
        }

        review_response = requests.get(review_url.format(
            restaurant_id), headers=header).json()

        review_array = review_response['user_reviews']
        length = len(review_array)
        reviews = []

        for i in range(0, length):
            review_obj = review_array[i]['review']

            if review_obj['rating_text'] != 'Insane!':
                rating_color = review_obj['rating_color']
            else:
                rating_color = '13FF00'

            review = {
                'user_name': review_obj['user']['name'],
                'profile_image': review_obj['user']['profile_image'],
                'foodie_level': review_obj['user']['foodie_level'],
                'foodie_color': review_obj['user']['foodie_color'],
                'timestamp': review_obj['review_time_friendly'],
                'review_text': review_obj['review_text'],
                'rating': review_obj['rating'],
                'rating_text': review_obj['rating_text'],
                'rating_color': rating_color
            }
            reviews.append(review)

        static_map_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=14&size=300x300&maptype=roadmap&markers=color:red%7Clabel:R%7C{},{}&key={}'
        context = {
            'static_map_url': static_map_url.format(lat, lng, google_static_map_api, google_static_map_signature),
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


def search(request):

    url = 'https://developers.zomato.com/api/v2.1/search?entity_id=3&entity_type=city&q={}&lat={}&lon={}&radius={}&sort=real_distance'
    header = {
        'user-key': api_key
    }

    restaurants = []
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = name.replace(' ', '%20')
            address = form.cleaned_data['address']
            address = address.replace(' ', '%20')
            print(name, address)

            lat = ''
            lng = ''
            radius = ''

            if address != None:
                print(address)
                google_maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={}&key={}'
                print(google_maps_url.format(address, stolen_api))
                geocoding_result = requests.get(google_maps_url.format(address, temp_api)).json()
                if geocoding_result['status'] == 'OK':
                    lat = geocoding_result['results'][0]['geometry']['location']['lat']
                    lng = geocoding_result['results'][0]['geometry']['location']['lng']
                    radius = 2000
                    print(lat)
                    print(lng)
                else:
                    print(geocoding_result['error_message'])
                    
            else:
                print('Empty')

            print(url.format(name, lat, lng, radius))
            response = requests.get(url.format(name, lat, lng, radius), headers=header).json()

            restaurant_array = response['restaurants']
            length = len(restaurant_array)

            
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

    else:
        form = RestaurantForm()

    context = {
        'form': form,
        'restaurants': restaurants
    }
    return render(request, 'DJEats/search.html', context)


def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
