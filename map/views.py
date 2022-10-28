from django.shortcuts import render
import folium as fol
import geocoder as geo

# Create your views here.

def map_view(request):
    location  = geo.osm('IN')
    laitude   = location.lat
    longitude = location.lng
    country   = location.country
    print(laitude,'----')
    # Create map objects
    map = fol.Map(location=[19, -12], zoom_start = 2)
    fol.Marker([laitude, longitude], tooltip = 'Click for details', popup = f'<a href="#">{country}<a>').add_to(map)
    # Htmp representation of teh map object
    map = map._repr_html_()
    context = {
        'map' : map
    }
    return render(request, 'map/map_index.html', context = context)

