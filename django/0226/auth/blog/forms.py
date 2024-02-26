from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField()
    contents = forms.CharField()

    class Meta :
        model = Post
        fields = ['title', 'contents', 'main_image'] 
        # fields = '__all__'