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
    path('edit-devise/<int:pk>/', v.edit_devise, name = "edit-devise"),
    path('device-list/', v.devise_list, name = "device-list"),
    path('device-list/', v.devise_list, name = "device-list"),
    path('device-details/<int:pk>/', v.devise_details, name = "device-details"),
    path('api-overview/<int:pk>/', v.api_overview, name = "api-overview"),
    path('api-edit/<int:pk>/', v.UpdateApi.as_view(), name = "api-edit"),
    path('api-list/<int:pk>/', v.api_list, name = "api-list"),
    # path('device-details1/', TemplateView.as_view(template_name="device_details.html"), name = "device-details1"),
    path('users/',v.users, name = "users"),
    path('forgot_password/', TemplateView.as_view(template_name="forgot_password.html"), name = "forgot_password"),
    path('dsahboard/', TemplateView.as_view(template_name="dashboard.html"), name = "dsahboard"),
    path('notifications/', v.notifications, name = "notifications"),
    path('notifications/<int:pk>/', v.notifications, name = "notifications"),
]

