from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic.base import ContextMixin

from wykop.accounts.forms import RegisterForm
from django.contrib.auth.views import LoginView as DjangoLoginView


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().dispatch(request, *args, **kwargs)

class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().dispatch(request, *args, **kwargs)

