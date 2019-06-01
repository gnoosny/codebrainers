from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, View
from django.views.generic.base import ContextMixin

from wykop.accounts.forms import RegisterForm
from wykop.accounts.models import User


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

class BanUserView(View):
    template_name = 'accounts/ban.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        print('request.POST')
        print(request.POST)
        print('kwargs')
        print(kwargs)
        

        u = User.objects.get(pk=kwargs.get('user_pk'))
        u.banned = request.POST.get('set') == '1'
        u.save()
        

        return redirect(
            request.META.get('HTTP_REFERER', reverse('posts:list'))
        )
