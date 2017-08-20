from django import forms
from .widgets import SimpleMDE
from .models import Post, Comment


class ArticleAdminModelForm(forms.ModelForm):
    markdown_text = forms.CharField(widget=SimpleMDE())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
                'markdown_text':SimpleMDE(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content',]
