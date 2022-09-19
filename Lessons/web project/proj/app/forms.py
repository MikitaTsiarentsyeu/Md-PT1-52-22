
from django import forms
from .models import Post

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label='Title', required=False)
    subtitle = forms.CharField(max_length=200)
    content = forms.CharField()
    image = forms.ImageField()
    post_theme = forms.ChoiceField(choices=Post.POST_THEMES)

class AddPostViaModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'image', 'post_theme')