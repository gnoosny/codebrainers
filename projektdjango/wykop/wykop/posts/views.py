from datetime import timedelta
from time import timezone

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, TemplateView, UpdateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

from .models import Post, Vote

# def hello_world(request):
#     # return HttpResponse('<div style="text-align:center; width: 100%;"><h1><b>Hello world!</b></h1></div>')
#     # print(request)
#     return render(request, 'posts/index.html')

# class HelloWorldView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'posts/index.html')

class HelloWorldView(TemplateView):
    template_name = 'base.html'

class PostList(ListView):
    template_name = 'posts/list.html'
    model = Post
    paginate_by = 3
    ordering = '-date'
    extra_context = {
        'title': "Posts ",
    }

class TopPostsList(PostList):
    queryset = Post.objects.annotate(score=Coalesce(Sum('votes__value'), 0)).order_by('-score')
    ordering = ''

class PostView(DetailView):
    template_name = 'posts/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.title
        return data

class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'posts/add.html'
    model = Post
    fields = ['title', 'content', 'image', 'video']
    extra_context = {
        'title': "Add ",
    }


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['title', 'content', 'image']


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Edit ' + self.object.title
        return data

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Delete ' + self.object.title
        return data

    def test_func(self):
        obj = self.get_object()
        return (
            (self.request.user == obj.author) and
            (timezone.now() - obj.date < timedelta(0, 60*15))
        )

class VoteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        post_pk = kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_pk)
        value = request.POST.get('value')
        Vote.objects.update_or_create(
            user=user, post=post,
            defaults={
                'value': value
            }
        )
        return redirect(post)