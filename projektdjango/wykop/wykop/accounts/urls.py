from django.contrib.auth.views import LogoutView
from django.urls import path

from wykop.accounts.views import RegisterView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    path('register', RegisterView.as_view(), name = 'register')
]
