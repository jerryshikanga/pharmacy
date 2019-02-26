from django.urls import path
from pharmacy.apps.profiles import views as profile_views

app_name = "profiles"

urlpatterns = [
    path("register/", profile_views.UserCreateView.as_view(), name="user_create")
]
