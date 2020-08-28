from django.shortcuts import render
import requests
# Create your views here.
def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5b0f0fbdbbd992b29754e9acb1ec66eb'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #recibe los datos de la api y los convierte a json

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}
    return render(request, 'climaApp/index.html')