from django.contrib.auth.forms import UserCreationForm, UsernameField

from wykop.accounts.models import User


class RegisterForm(UserCreationForm):

    class Meta:
            model = User
            fields = ("username", 'email')
            field_classes = {'username': UsernameField}
