from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

# def hello_world(request):
#     # return HttpResponse('<div style="text-align:center; width: 100%;"><h1><b>Hello world!</b></h1></div>')
#     # print(request)
#     return render(request, 'posts/index.html')

# class HelloWorldView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'posts/index.html')

class HelloWorldView(TemplateView):
    template_name = 'posts/index.html'