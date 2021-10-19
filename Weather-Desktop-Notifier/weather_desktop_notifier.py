# Weather Desktop Notifier - Fetches the weather updates of a city and displays a notification
# on the desktop with live weather updates (temperature, wind, and humidity). The script
# notifies the user every 2 hours until the user stops the execution of the program.

# Note: Weather updates can be seen only for the major cities which are listed below.
# [Mumbai, Bengaluru, Chennai, Hyderabad, Kolkata, Ahmedabad, Pune, Delhi]

import requests
from bs4 import BeautifulSoup
import geocoder
from geopy.geocoders import Nominatim
from win10toast import ToastNotifier
import time


while True:
    # Set the url from where the weather data needs to be fetched.
    url = "https://mausam.imd.gov.in/"

    # Get the HTML source code.
    html_source_code = requests.get(url).text

    # Create BeautifulSoup object with html parser.
    soup = BeautifulSoup(html_source_code, "html.parser")

    # Get the current city of the user.
    location = geocoder.ip('me')
    latitude, longitude = (location.latlng[0], location.latlng[1])
    coordinates = str(latitude) + ", " + str(longitude)
    geolocator = Nominatim(user_agent="weather_desktop_notifier")
    location_name = geolocator.reverse(coordinates, language="en").raw
    current_city = location_name['address']['city']

    # Scrap the web page to find the given city.
    cities = soup.find_all("div", attrs={'class': 'capital'})
    cities_txt = [city.text for city in cities]
    cleaned_city_names = []
    for city in cities_txt:
        index = city.index(" ")
        cleaned = city[1:index]
        cleaned_city_names.append(cleaned)

    # Find the the current users' city in the major cities list.
    for city_name in cleaned_city_names:
        # If the city is found, then generate the desktop notification.
        if city_name == current_city:
            index = cleaned_city_names.index(city_name)
            city_div = cities[index]
            city_temperature = (city_div.find("span", attrs={'class': 'val'})).text
            city_wind = (city_div.find("p", attrs={'class': 'wind'})).text
            city_humidity = (city_div.find("p", attrs={'class': 'minmax'})).text
            city_humidity = city_humidity.strip()
            result = city_name + "\n" + \
                     "Temperature: " + city_temperature + "\n" + \
                     "Wind: " + city_wind + "\n" + \
                     "Humidity: " + city_humidity + "\n"

            # Create a ToastNotifier object to show the desktop notification.
            notifier = ToastNotifier()
            notifier.show_toast("Live Weather Update", result, duration=20)
            break
    else:
        result = "Weather updates could not be fetched for your location.\nYou may visit online " \
                 "resources for weather updates of your city/location."
        notifier = ToastNotifier()
        notifier.show_toast("Live Weather Update", result, duration=20)

    # Wait for 7180 seconds (approx 2 hours) before showing another notification.
    time.sleep(7180)
