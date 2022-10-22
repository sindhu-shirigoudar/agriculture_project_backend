# from django.urls import path, include
# from .views import index
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home1.html"), name = "home"),
    path('login/', TemplateView.as_view(template_name="login.html"), name = "login"),
    path('acess_denied/', TemplateView.as_view(template_name="acess_denied.html"), name = "acess_denied"),
    path('c/', TemplateView.as_view(template_name="register.html"), name = "c"),
]

