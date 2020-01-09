# Djomato

## About

A web project developed using Django showcasing popular nearby restaurants using Zomato API.

The user can search for restaurants in any location using the search bar powered by Google Places Autocomplete API.
The address will be auto converted to latitude and longitude by Google Geocoding API. He/she can see the details of each restaurant and basic information including reviews and location of the restaurant in a static map provided by Google Maps Static API.

Users are created by the default Django User Model, and data is saved in SQLite3.

## Pre-requisites

-   [Zomato API](https://developers.zomato.com/api)
-   [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/start)
-   [Google Maps Static API](https://developers.google.com/maps/documentation/maps-static/intro)
-   [Google Places Autocomplete API](https://developers.google.com/places/web-service/autocomplete)

## Technology Stack

1. Developed using Django
1. Restaurant data provided by Zomato API
1. Location geocoded by Google Geocoding API
1. Locations generated in search bar by Google Places Autocomplete API
1. Location of restaurant provided by Google Maps Static API

## Build

-   `Djomato/DJEats/views.py`

    -   Put your Zomato API key in `api_key`

    -   Put your Google Maps Static API key in `google_static_map_api`

    -   Put your Google Maps Static API signature in `google_static_map_signature`

    -   Put your Google Geocoding API key in `google_maps_api_key`

    -   Put your default latitude in `latitude`

    -   Put your default longitude in `longitude`

-   `Djomato/DJEats/templates/base.html`

    -   Put your Google Autocomplete API key in `<script src>` in `<body>`

-   `Djomato/Djomato/settings.py`
    -   Put your secret key in `SECRET_KEY`

```bash
python manage.py runserver
```

## Developers

> Adnan Hakim
> [github.com/adnanhakim](https://github.com/adnanhakim)

> Arsh Shaikh
> [github.com/arshshaikh06](https://github.com/arshshaikh06)

## MIT LICENSE

> Copyright (c) 2019 Adnan Hakim
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
