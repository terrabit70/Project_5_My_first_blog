from django import forms

from .models import Post, Comment
from blog.scripts.brackets_validator import Validator as BracketsValidator

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class BracketsValidatorForm(forms.Form):
    brackets = forms.CharField()
    text_to_validate = forms.CharField(widget=forms.Textarea())

