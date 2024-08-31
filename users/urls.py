from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from django.urls import path

from users.views import UserCreateView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserCreateView.as_view(), name='registration'),
]
