from django.urls import path, include
from . import views
from knox import views as knox_views

app_name = "users"

urlpatterns = [
    path("register/", views.RegistrationAPI.as_view(), name="user-register"),
    path("login/", views.LoginAPI.as_view(), name="user-login"),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("user/", views.UserAPI.as_view(), name="user-data"),
]