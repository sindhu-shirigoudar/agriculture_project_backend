from django.shortcuts import render
import folium as fol
import geocoder as geo
import os
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login1/')    
def map_view(request):
    location  = geo.osm('IN')
    laitude   = location.lat
    longitude = location.lng
    country   = location.country
    # Create map objects
    map = fol.Map(location=[laitude, longitude], zoom_start = 5)
    fol.Marker([laitude, longitude], tooltip = f'Click for details', popup = f'<a href="#">{country}<a>', icon=fol.Icon(color="blue"),).add_to(map)
    # Htmp representation of teh map object
    map = map._repr_html_()
    context = {
        'map' : map
    }
    return render(request, 'map/map_index.html', context = context)

