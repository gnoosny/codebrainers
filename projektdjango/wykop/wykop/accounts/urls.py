from django.contrib.auth.views import LogoutView
from django.urls import path

from wykop.accounts.views import RegisterView, LoginView, BanUserView

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    path('register', RegisterView.as_view(), name = 'register'),
    path('ban/<int:user_pk>', BanUserView.as_view(), name = 'ban')
]
