from django.shortcuts import render
import folium as fol
import geocoder as geo
import os
from django.contrib.auth.decorators import login_required
from agriapp.models import DeviseLocation, Devise, DeviseApis

# Create your views here.

@login_required(login_url='/login1/')    
def map_view(request, **kwargs):
    location  = geo.osm('IN')
    latitude   = location.lat
    longitude = location.lng
    country   = location.country
    map = fol.Map(location=[latitude, longitude], zoom_start = 6)
    fol.Marker([latitude, longitude], tooltip = f'India', popup = f'{country}', icon=fol.Icon(color="blue"),).add_to(map)
    if kwargs:
        devise_id = kwargs['pk']
        location = DeviseLocation.objects.filter(status=True, devise__pk = devise_id)
        if location:
            latitude  = location.latitude
            longitude = location.longitude
            map       = fol.Map(location=[latitude, longitude], zoom_start = 6)
            fol.Marker([latitude, longitude], tooltip = f'Click for details', popup = f'{location.device.name}', icon=fol.Icon(color="blue"),).add_to(map)
        
    # Create map objects
    
    # Htmp representation of teh map object
    map = map._repr_html_()
    context = {
        'map' : map
    }
    return render(request, 'map/map_index.html', context = context)

