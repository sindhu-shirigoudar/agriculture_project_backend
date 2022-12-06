# from django.urls import path, include
# from .views import index
from django.urls import path
from django.views.generic import TemplateView
from . import views as v

urlpatterns = [
    path('',  v.home, name = "home"),
    path('login/', TemplateView.as_view(template_name="login.html"), name = "login"),
    path('login1/', v.login, name = "login1"),
    path('logout/', v.logout, name = "logout"),
    path('acess_denied/', TemplateView.as_view(template_name="acess_denied.html"), name = "acess_denied"),
    path('register/', TemplateView.as_view(template_name="register.html"), name = "register"),
    path('add-devise/', v.add_devise, name = "add-devise"),
    path('device-list/', TemplateView.as_view(template_name="device_list.html"), name = "device-details"),
    path('device-details/', TemplateView.as_view(template_name="device_details.html"), name = "device-list"),
    path('users/',v.users, name = "users"),
    path('forgot_password/', TemplateView.as_view(template_name="forgot_password.html"), name = "forgot_password"),
]

