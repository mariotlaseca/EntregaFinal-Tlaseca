from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from usuarios_app.views import *

urlpatterns = [
    path("login/", LoginView.as_view(template_name= "usuarios_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name= "usuarios_app/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/change", profile_change, name="profile_edit"),
]