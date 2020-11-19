from django.shortcuts import render
from django.views.generic import  ListView, DeleteView
from . import  models
# from django.http import HttpResponse
# Create your views here.
# def home(req):
#     return render(req, 'home.html', {})
class HomeView(ListView):
    model = models.Post
    template_name = 'home.html'

class ArticleDetailView(DeleteView):
    model = models.Post
    template_name = 'article_details.html'
