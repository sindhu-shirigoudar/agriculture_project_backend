from django.shortcuts import render
import folium as f

# Create your views here.

def map_view(request):
    # create map objects
    map = f.Map()
    map = map._repr_html_()
    context = {
        'map' : map
    }
    return render(request, 'map/map_index.html', context = context)

