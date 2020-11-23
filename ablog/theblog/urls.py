from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('article/<pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', views.AddPostView.as_view(), name='add-post'),
    path('article/edit/<pk>', views.EditPostView.as_view(), name='edit-post'),
    path('article/delete/<pk>', views.DeletePostView.as_view(), name='delete-post'),
]