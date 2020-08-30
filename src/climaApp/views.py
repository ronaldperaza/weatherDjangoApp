import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):

    cities = City.objects.all() #return all the cities in the database
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=aedb90cbf97e483936b340d0c0ff42f8'
    
    if request.method == 'POST': #cuando el formulario es enviado
        form = CityForm(request.POST) #agrega la solicitud de datos para procesarlos
        form.save() #valida y guarda
    
    form = CityForm()
    weather_data = []
    
    for city in cities:

        city_weather = requests.get(url.format(city)).json() #recibe los datos de la api y los convierte a json
        
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather) #agrega la data para la actual ciudad en la lista

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'climaApp/index.html', context)
    
