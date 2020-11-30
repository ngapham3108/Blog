from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import  reverse_lazy
from django.shortcuts import  redirect
# from django.http import HttpResponse
# Create your views here.
# def home(req):
#     return render(req, 'home.html', {})
class HomeView(ListView):
    model = models.Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        try:
            cat_menu = models.Category.objects.all()
        except:
            cat_menu = {}
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context



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
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        if str(request.user.id) != kwargs['pk']:
            return redirect(reverse_lazy('home'))
        else:
            return super().get(request, *args, **kwargs)

class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        if str(request.user.id) != kwargs['pk']:
            return redirect(reverse_lazy('home'))
        else:
            return super().get(request, *args, **kwargs)

def CategoryView(req, cat):
    try:
        cat_posts = models.Post.objects.filter(cats=cat)
    except:
        cat_posts = {}
    try:
        cat_menu = models.Category.objects.all()
    except:
        cat_posts = {}

    return render(req, 'category_filter.html', {'post_list': cat_posts, 'cat_menu': cat_menu})
