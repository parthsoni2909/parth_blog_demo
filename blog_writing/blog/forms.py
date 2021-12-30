from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    #name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name'}))
    #body = forms.CharField(widget=forms.Textarea(attrs={'id': 'body'}))

    class Meta:
        model = Comment
        fields = ('body',)