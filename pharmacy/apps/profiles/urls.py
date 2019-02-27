from django.urls import path
from pharmacy.apps.profiles import views as profile_views

app_name = "profiles"

urlpatterns = [
    path('register/', profile_views.RegisterUser.as_view(), name='register_user'),
    path('register/success.html', profile_views.success_user_create, name='register_success'),
    path('profile/', profile_views.profile, name='profile'),
    path('profile/update/<int:id>/', profile_views.UpdateAccount.as_view(), name='account_update'),
]
