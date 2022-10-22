# from django.urls import path, include
# from .views import index
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home1.html"), name = "home"),
    path('login/', TemplateView.as_view(template_name="login.html"), name = "login"),
]

