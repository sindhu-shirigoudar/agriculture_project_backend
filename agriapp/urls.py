# from django.urls import path, include
# from .views import index
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home1.html"), name = "home"),
    path('login/', TemplateView.as_view(template_name="login.html"), name = "login"),
    path('login1/', TemplateView.as_view(template_name="login1.html"), name = "login1"),
    path('acess_denied/', TemplateView.as_view(template_name="acess_denied.html"), name = "acess_denied"),
    path('register/', TemplateView.as_view(template_name="register.html"), name = "register"),
    path('register-1/', TemplateView.as_view(template_name="register_1.html"), name = "register-1"),
    path('device-list/', TemplateView.as_view(template_name="device_list.html"), name = "device-details"),
    path('device-details/', TemplateView.as_view(template_name="device_details.html"), name = "device-list"),
    path('users/', TemplateView.as_view(template_name="users.html"), name = "users"),
    path('forgot_password/', TemplateView.as_view(template_name="forgot_password.html"), name = "forgot_password"),
]

