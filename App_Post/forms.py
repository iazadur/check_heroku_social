from django import forms
from App_Post.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['caption', 'image']