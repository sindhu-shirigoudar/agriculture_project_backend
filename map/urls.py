from django.urls import path
from map import views as v

urlpatterns = [
    path('map/', v.map_view, name = "map"),
]