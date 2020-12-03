from django import forms
from .models import Post, Category
choices = []
try:
    list_category = Category.objects.all()
    for cat in list_category:
        choices.append((cat.name, cat.name))
except:
    pass
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'cats', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'type': 'hidden'}),
            'cats': forms.Select(choices=choices),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'cats', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of your blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'cats': forms.Select(choices=choices),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }