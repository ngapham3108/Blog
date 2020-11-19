from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('article/<pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', views.AddPostView.as_view(), name='add-post'),
    path('editpost/<pk>', views.EditPostView.as_view(), name='edit-post'),
]