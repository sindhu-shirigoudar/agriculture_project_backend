from django.urls import path
from . import views as v

urlpatterns = [
    path('list/',  v.get_api_list, name = "home"),  
    path('add_location/',  v.add_location, name = "add_location"),  
    path('get_devise_by_devise_id/',  v.get_devise_by_devise_id, name = "get_devise_by_devise_id"),  
    path('add_soil_data/',  v.add_soil_data, name = "add_soil_data"),  
]

