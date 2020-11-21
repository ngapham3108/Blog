from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import  reverse_lazy
# from django.http import HttpResponse
# Create your views here.
# def home(req):
#     return render(req, 'home.html', {})
class HomeView(ListView):
    model = models.Post
    template_name = 'home.html'
    ordering = ['pk']

class ArticleDetailView(DetailView):
    model = forms.Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'

class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.EditForm
    template_name = 'edit_post.html'

class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
