from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms
# from django.http import HttpResponse
# Create your views here.
# def home(req):
#     return render(req, 'home.html', {})
class HomeView(ListView):
    model = models.Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = forms.PostForm
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'

